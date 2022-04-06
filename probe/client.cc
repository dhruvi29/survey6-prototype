#include <string>
#include <pcap.h>
#include <netinet/in.h>
#include <netinet/if_ether.h>
#include <grpcpp/grpcpp.h>
#include "cmake/build/ip6.grpc.pb.h"
#include "time.h"
#include <iostream>
#include <vector>
#include <thread>
#include <queue>


using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using ip6::Packet;
using ip6::Artery;
using ip6::Heart;
using ip6::Vein;
using ip6::PacketRequest;
using ip6::PacketRecieved;

using namespace std;

class PacketClient {
    public:
        PacketClient(std::shared_ptr<Channel> channel) : stub_(Packet::NewStub(channel)) {}

    int sendPacket(int a, int b) {
        PacketRequest request;

        request.set_a(a);
        request.set_b(b);

        PacketRecieved reply;

        ClientContext context;

        Status status = stub_->sendPacket(&context, request, &reply);

        if(status.ok()){
            return reply.result();
        } else {
            std::cout<<"punch";
            std::cout << status.error_code() << ": " << status.error_message() << std::endl;
            return -1;
        }
    }

    private:
        std::unique_ptr<Packet::Stub> stub_;
};


class HeartClient {
    public:
        HeartClient(std::shared_ptr<Channel> channel) : stub_(Heart::NewStub(channel)) {}

    int sendHeartBeat() {
        Artery request;

        request.set_a(1);

        Vein reply;

        ClientContext context;

        Status status = stub_->sendHeartBeat(&context, request, &reply);

        if(status.ok()){
            return reply.a();
        } else {
            std::cout << status.error_code() << ": " << status.error_message() << std::endl;
            return -1;
        }
    }

    private:
        std::unique_ptr<Heart::Stub> stub_;
};


void CapturePackets();
void SendPackets();
void HeartBeats();
pcap_t* connectDevice();
void got_packet(u_char *args, const struct pcap_pkthdr *header,const u_char *packet);
time_t start = time(NULL);
queue<char> pkts;


int main(int argc, char* argv[]){

    thread capPkt(CapturePackets);
    thread sendPkt(SendPackets);
    thread heart(HeartBeats);
    capPkt.join();
    sendPkt.join();
    heart.join();

    return 0;
}
void HeartBeats(){
    std::string address("localhost:50051");

    HeartClient client(grpc::CreateChannel(
            address, 
            grpc::InsecureChannelCredentials()
        ));
    while(true){
        client.sendHeartBeat();
        sleep(2);
    }
}
void CapturePackets(){
    pcap_t *handle = connectDevice();
    if(handle == NULL)return;
    pcap_loop(handle, 100, got_packet, NULL);  
}

void SendPackets(){

    std::string address("localhost:50051");
    PacketClient client(
        grpc::CreateChannel(
            address, 
            grpc::InsecureChannelCredentials()
        )
    );

    while(true){
        auto t = time(NULL) - start;
        std::cout<<t<<"\n";
        if(t >= 5 && !pkts.empty()){
            client.sendPacket(1,2);
            pkts.pop();
        }
    }

}

void got_packet(u_char *args, const struct pcap_pkthdr *header,const u_char *packet){
    pkts.push(0);
    start = time(NULL);
}

pcap_t* connectDevice(){
    char error_buffer[PCAP_ERRBUF_SIZE];
    pcap_if_t *alldevsp, *devs_copy;
    int error;
    bpf_u_int32 ip_raw;         
    bpf_u_int32 subnet_mask_raw;
    char ip[13];
    char subnet_mask[13];
    struct in_addr address;
    char *device;
    pcap_t *handle;
    const u_char *packet;
    struct pcap_pkthdr packet_header;
    int packet_count_limit = 1;
    int timeout_limit = 1000; 
    struct bpf_program fp;		
    // Possible protocols are: ether, fddi, tr, wlan, ip, ip6, arp, rarp, decnet, sctp, tcp and udp. 
    char filter_exp[] = "ip";	

    error = pcap_findalldevs(&alldevsp, error_buffer);
    if (error == PCAP_ERROR)
    {
        printf("Error finding device: %s\n", error_buffer);
        return handle;
    }
    devs_copy = alldevsp;

    if (alldevsp->flags == PCAP_IF_WIRELESS)
        printf("its wireless\n");

    device = devs_copy->next->name;

    error = pcap_lookupnet(
        device,
        &ip_raw,
        &subnet_mask_raw,
        error_buffer);
    if (error == -1)
    {
        printf("%s\n", error_buffer);
        return handle;
    }
    address.s_addr = ip_raw;
    strcpy(ip, inet_ntoa(address));
    if (ip == NULL)
    {
        perror("inet_ntoa");
        return handle;
    }

    address.s_addr = subnet_mask_raw;
    strcpy(subnet_mask, inet_ntoa(address));
    if (subnet_mask == NULL)
    {
        perror("inet_ntoa");
        return handle;
    }

    printf("Device: %s\n", device);
    printf("IP address: %s\n", ip);
    printf("Subnet mask: %s\n", subnet_mask);
    printf("0\n");

    handle = pcap_open_live(
        device,
        BUFSIZ,
        packet_count_limit,
        timeout_limit,
        error_buffer);
    printf("1\n");
    
    if(handle == NULL){
        printf("Cannot oprn device %s",error_buffer);
        return handle;
    }
    printf("2\n");

    if (pcap_compile(handle, &fp, filter_exp, 0, ip_raw) == -1) {
        fprintf(stderr, "Couldn't parse filter %s: %s\n", filter_exp, pcap_geterr(handle));
        return handle;
    }
    printf("3\n");


    if (pcap_setfilter(handle, &fp) == -1) {
        fprintf(stderr, "Couldn't install filter %s: %s\n", filter_exp, pcap_geterr(handle));
        return handle;
    }
    printf("returning handle\n");

    return handle;
}