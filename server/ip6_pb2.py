# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ip6.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tip6.proto\x12\x03ip6\"\x13\n\x06\x41rtery\x12\t\n\x01\x61\x18\x01 \x01(\x05\"\x11\n\x04Vein\x12\t\n\x01\x61\x18\x01 \x01(\x05\"%\n\rPacketRequest\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\" \n\x0ePacketRecieved\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\x41\n\x06Packet\x12\x37\n\nsendPacket\x12\x12.ip6.PacketRequest\x1a\x13.ip6.PacketRecieved\"\x00\x32\x32\n\x05Heart\x12)\n\rsendHeartBeat\x12\x0b.ip6.Artery\x1a\t.ip6.Vein\"\x00\x42\t\n\x07\x65x.grpcb\x06proto3')



_ARTERY = DESCRIPTOR.message_types_by_name['Artery']
_VEIN = DESCRIPTOR.message_types_by_name['Vein']
_PACKETREQUEST = DESCRIPTOR.message_types_by_name['PacketRequest']
_PACKETRECIEVED = DESCRIPTOR.message_types_by_name['PacketRecieved']
Artery = _reflection.GeneratedProtocolMessageType('Artery', (_message.Message,), {
  'DESCRIPTOR' : _ARTERY,
  '__module__' : 'ip6_pb2'
  # @@protoc_insertion_point(class_scope:ip6.Artery)
  })
_sym_db.RegisterMessage(Artery)

Vein = _reflection.GeneratedProtocolMessageType('Vein', (_message.Message,), {
  'DESCRIPTOR' : _VEIN,
  '__module__' : 'ip6_pb2'
  # @@protoc_insertion_point(class_scope:ip6.Vein)
  })
_sym_db.RegisterMessage(Vein)

PacketRequest = _reflection.GeneratedProtocolMessageType('PacketRequest', (_message.Message,), {
  'DESCRIPTOR' : _PACKETREQUEST,
  '__module__' : 'ip6_pb2'
  # @@protoc_insertion_point(class_scope:ip6.PacketRequest)
  })
_sym_db.RegisterMessage(PacketRequest)

PacketRecieved = _reflection.GeneratedProtocolMessageType('PacketRecieved', (_message.Message,), {
  'DESCRIPTOR' : _PACKETRECIEVED,
  '__module__' : 'ip6_pb2'
  # @@protoc_insertion_point(class_scope:ip6.PacketRecieved)
  })
_sym_db.RegisterMessage(PacketRecieved)

_PACKET = DESCRIPTOR.services_by_name['Packet']
_HEART = DESCRIPTOR.services_by_name['Heart']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\007ex.grpc'
  _ARTERY._serialized_start=18
  _ARTERY._serialized_end=37
  _VEIN._serialized_start=39
  _VEIN._serialized_end=56
  _PACKETREQUEST._serialized_start=58
  _PACKETREQUEST._serialized_end=95
  _PACKETRECIEVED._serialized_start=97
  _PACKETRECIEVED._serialized_end=129
  _PACKET._serialized_start=131
  _PACKET._serialized_end=196
  _HEART._serialized_start=198
  _HEART._serialized_end=248
# @@protoc_insertion_point(module_scope)
