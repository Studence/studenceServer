# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parentsPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import namePb_pb2 as namePb__pb2
import mobilePb_pb2 as mobilePb__pb2
import parentsUiPb_pb2 as parentsUiPb__pb2
import emailPb_pb2 as emailPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='parentsPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0fparentsPb.proto\x1a\x0cnamePb.proto\x1a\x0emobilePb.proto\x1a\x11parentsUiPb.proto\x1a\remailPb.proto\"\x91\x01\n\tParentsPb\x12\x15\n\x04name\x18\x01 \x01(\x0b\x32\x07.NamePb\x12\x19\n\x06mobile\x18\x02 \x03(\x0b\x32\t.MobilePb\x12\x17\n\x05\x65mail\x18\x03 \x01(\x0b\x32\x08.EmailPb\x12\x13\n\x0bparentsCode\x18\x04 \x01(\t\x12$\n\nparentType\x18\x05 \x01(\x0e\x32\x10.ParentsTypeEnumb\x06proto3'
  ,
  dependencies=[namePb__pb2.DESCRIPTOR,mobilePb__pb2.DESCRIPTOR,parentsUiPb__pb2.DESCRIPTOR,emailPb__pb2.DESCRIPTOR,])




_PARENTSPB = _descriptor.Descriptor(
  name='ParentsPb',
  full_name='ParentsPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ParentsPb.name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='ParentsPb.mobile', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='ParentsPb.email', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentsCode', full_name='ParentsPb.parentsCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentType', full_name='ParentsPb.parentType', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=84,
  serialized_end=229,
)

_PARENTSPB.fields_by_name['name'].message_type = namePb__pb2._NAMEPB
_PARENTSPB.fields_by_name['mobile'].message_type = mobilePb__pb2._MOBILEPB
_PARENTSPB.fields_by_name['email'].message_type = emailPb__pb2._EMAILPB
_PARENTSPB.fields_by_name['parentType'].enum_type = parentsUiPb__pb2._PARENTSTYPEENUM
DESCRIPTOR.message_types_by_name['ParentsPb'] = _PARENTSPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParentsPb = _reflection.GeneratedProtocolMessageType('ParentsPb', (_message.Message,), {
  'DESCRIPTOR' : _PARENTSPB,
  '__module__' : 'parentsPb_pb2'
  # @@protoc_insertion_point(class_scope:ParentsPb)
  })
_sym_db.RegisterMessage(ParentsPb)


# @@protoc_insertion_point(module_scope)
