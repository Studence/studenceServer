# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entityPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timeUiPb_pb2 as timeUiPb__pb2
import entityUiPb_pb2 as entityUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entityPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x65ntityPb.proto\x1a\x0etimeUiPb.proto\x1a\x10\x65ntityUiPb.proto\"a\n\x08\x45ntityPb\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x1d\n\x08lifeTime\x18\x03 \x01(\x0e\x32\x0b.StatusEnum\x12\x19\n\x06locale\x18\x04 \x01(\x0b\x32\t.LocalePb\"2\n\x08LocalePb\x12&\n\x0f\x64\x65\x66\x61ultTimeZone\x18\x01 \x01(\x0e\x32\r.TimeZoneEnumb\x06proto3'
  ,
  dependencies=[timeUiPb__pb2.DESCRIPTOR,entityUiPb__pb2.DESCRIPTOR,])




_ENTITYPB = _descriptor.Descriptor(
  name='EntityPb',
  full_name='EntityPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EntityPb.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='EntityPb.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifeTime', full_name='EntityPb.lifeTime', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locale', full_name='EntityPb.locale', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=52,
  serialized_end=149,
)


_LOCALEPB = _descriptor.Descriptor(
  name='LocalePb',
  full_name='LocalePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='defaultTimeZone', full_name='LocalePb.defaultTimeZone', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=151,
  serialized_end=201,
)

_ENTITYPB.fields_by_name['lifeTime'].enum_type = entityUiPb__pb2._STATUSENUM
_ENTITYPB.fields_by_name['locale'].message_type = _LOCALEPB
_LOCALEPB.fields_by_name['defaultTimeZone'].enum_type = timeUiPb__pb2._TIMEZONEENUM
DESCRIPTOR.message_types_by_name['EntityPb'] = _ENTITYPB
DESCRIPTOR.message_types_by_name['LocalePb'] = _LOCALEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EntityPb = _reflection.GeneratedProtocolMessageType('EntityPb', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYPB,
  '__module__' : 'entityPb_pb2'
  # @@protoc_insertion_point(class_scope:EntityPb)
  })
_sym_db.RegisterMessage(EntityPb)

LocalePb = _reflection.GeneratedProtocolMessageType('LocalePb', (_message.Message,), {
  'DESCRIPTOR' : _LOCALEPB,
  '__module__' : 'entityPb_pb2'
  # @@protoc_insertion_point(class_scope:LocalePb)
  })
_sym_db.RegisterMessage(LocalePb)


# @@protoc_insertion_point(module_scope)
