# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genericRefUiPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nameUiPb_pb2 as nameUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='genericRefUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14genericRefUiPb.proto\x1a\x0enameUiPb.proto\"C\n\x0eGenericRefUiPb\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x04name\x18\x02 \x01(\x0b\x32\t.NameUiPb\x12\x0c\n\x04\x63ode\x18\x03 \x01(\tb\x06proto3'
  ,
  dependencies=[nameUiPb__pb2.DESCRIPTOR,])




_GENERICREFUIPB = _descriptor.Descriptor(
  name='GenericRefUiPb',
  full_name='GenericRefUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GenericRefUiPb.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='GenericRefUiPb.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='GenericRefUiPb.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=40,
  serialized_end=107,
)

_GENERICREFUIPB.fields_by_name['name'].message_type = nameUiPb__pb2._NAMEUIPB
DESCRIPTOR.message_types_by_name['GenericRefUiPb'] = _GENERICREFUIPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenericRefUiPb = _reflection.GeneratedProtocolMessageType('GenericRefUiPb', (_message.Message,), {
  'DESCRIPTOR' : _GENERICREFUIPB,
  '__module__' : 'genericRefUiPb_pb2'
  # @@protoc_insertion_point(class_scope:GenericRefUiPb)
  })
_sym_db.RegisterMessage(GenericRefUiPb)


# @@protoc_insertion_point(module_scope)