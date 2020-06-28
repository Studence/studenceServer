# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deviceInfoPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entityPb_pb2 as entityPb__pb2
import timePb_pb2 as timePb__pb2
import genericRefPb_pb2 as genericRefPb__pb2
import userTypeUiPb_pb2 as userTypeUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deviceInfoPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12\x64\x65viceInfoPb.proto\x1a\x0e\x65ntityPb.proto\x1a\x0ctimePb.proto\x1a\x12genericRefPb.proto\x1a\x12userTypeUiPb.proto\"\xc5\x01\n\x0c\x44\x65viceInfoPb\x12\x19\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\t.EntityPb\x12\x10\n\x08macAddId\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0e\n\x06osType\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x1c\n\x0b\x63reatedTime\x18\x06 \x01(\x0b\x32\x07.TimePb\x12\x1b\n\x04user\x18\x07 \x01(\x0b\x32\r.GenericRefPb\x12\x1f\n\x08userType\x18\x08 \x01(\x0e\x32\r.UserTypeEnumb\x06proto3'
  ,
  dependencies=[entityPb__pb2.DESCRIPTOR,timePb__pb2.DESCRIPTOR,genericRefPb__pb2.DESCRIPTOR,userTypeUiPb__pb2.DESCRIPTOR,])




_DEVICEINFOPB = _descriptor.Descriptor(
  name='DeviceInfoPb',
  full_name='DeviceInfoPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='DeviceInfoPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='macAddId', full_name='DeviceInfoPb.macAddId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='DeviceInfoPb.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osType', full_name='DeviceInfoPb.osType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='DeviceInfoPb.state', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdTime', full_name='DeviceInfoPb.createdTime', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='DeviceInfoPb.user', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userType', full_name='DeviceInfoPb.userType', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=290,
)

_DEVICEINFOPB.fields_by_name['dbInfo'].message_type = entityPb__pb2._ENTITYPB
_DEVICEINFOPB.fields_by_name['createdTime'].message_type = timePb__pb2._TIMEPB
_DEVICEINFOPB.fields_by_name['user'].message_type = genericRefPb__pb2._GENERICREFPB
_DEVICEINFOPB.fields_by_name['userType'].enum_type = userTypeUiPb__pb2._USERTYPEENUM
DESCRIPTOR.message_types_by_name['DeviceInfoPb'] = _DEVICEINFOPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceInfoPb = _reflection.GeneratedProtocolMessageType('DeviceInfoPb', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFOPB,
  '__module__' : 'deviceInfoPb_pb2'
  # @@protoc_insertion_point(class_scope:DeviceInfoPb)
  })
_sym_db.RegisterMessage(DeviceInfoPb)


# @@protoc_insertion_point(module_scope)
