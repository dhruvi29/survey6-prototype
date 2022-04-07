# Survey 6 ( Prototype )
This repo is a prototype for [Survey 6](https://github.com/web-telescope/survey6) project of [ScoreLabs](https://scorelab.org/)
<img src="https://github.com/dhruvi29/survey6-prototype/blob/main/screenshots/output3.gif" ></img></br>
Please find better quality video <a href = "https://drive.google.com/file/d/1pdec5jsAKsF6kJXJ16b1UgV-itqieYPz/view?usp=sharing"> here </a>




## About
### Description
Project: Ipv6 is the internet's future, and it necessitated a more scalable survey tool to comprehend how routing and DNS function. The purpose of this project is to create an IPv6 listener that will passively collect IPv6 traffic data as a passive data collection tool for cyber security research.
<br></br>
Prototype: In this protype, 
* The probe captures the IPv4 packets
* It sends dummy packet using gRPC requests to the server whenever the host network is idle for more than **5 seconds**.
* The probe sends heart beats to the server every **2 seconds** for health check. This is again done using gRPC. <br></br>
The server collects the pulses and logs them in the terminal.<br></br>
The server also logs the recieved dummy packet number.

## Output
<img src="https://github.com/dhruvi29/survey6-prototype/blob/main/screenshots/output1.png"/>
<img src="https://github.com/dhruvi29/survey6-prototype/blob/main/screenshots/output2.png"/>

### Tech Stack
1. libpcap
2. gRPC

### File Structure
```
.
├── ip6.proto
├── server
│   ├── server.py
├── probe
│   ├── CMakeLists.txt
│   └── client.cc
├── screenshots
└── README.md
```

## Requirements
1. You need version 3.13 or later of cmake. Install it by following these instructions:
```
sudo apt install -y cmake
cmake --version
```
2. Install the basic tools required to build gRPC:
```
sudo apt install -y build-essential autoconf libtool pkg-config
```
3. gRPC for C++ : follow [this](https://grpc.io/docs/languages/cpp/quickstart/) guide or follow the installation guide here
```
export MY_INSTALL_DIR=$HOME/.local
mkdir -p $MY_INSTALL_DIR
export PATH="$MY_INSTALL_DIR/bin:$PATH"
git clone --recurse-submodules -b v1.45.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
cd grpc
mkdir -p cmake/build
pushd cmake/build
cmake -DgRPC_INSTALL=ON \
      -DgRPC_BUILD_TESTS=OFF \
      -DCMAKE_INSTALL_PREFIX=$MY_INSTALL_DIR \
      ../..
make -j
make install
popd
```
4. Python 3.5 or higher
5. pip version 9.0.1 or higher 
6. Create Virtual Environment
```
python -m pip install virtualenv
virtualenv venv
source venv/bin/activate
```
7. gRPC for python : follow [this](https://grpc.io/docs/languages/python/quickstart/) guide or follow the installation guide here. Inside the virtual environment.
Install gRPC
```
python -m pip install grpcio
```
Install gRPC tools
```
python -m pip install grpcio-tools
```
<br></br>

> Current dependencies and requirements are as per linux based systems

## Usage
1. Activate the virtual environment
```
source venv/bin/activate
```
2. Clone the repository
```
git clone https://github.com/dhruvi29/survey6-prototype
cd survey6-prototype
```
3. Generate gRPC code for python server
```
cd server
python -m grpc_tools.protoc -I../ --python_out=. --grpc_python_out=. ../ip6.proto
```
4. Run Server
```
python server.py
```
5. Build probe - In a new terminal
```
cd probe
mkdir -p cmake/build
cd cmake/build
cmake -DCMAKE_PREFIX_PATH=$MY_INSTALL_DIR ../..
make
```
6. Run Probe
```
./client
```




