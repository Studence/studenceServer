# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: memberPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entityPb_pb2 as entityPb__pb2
import classPb_pb2 as classPb__pb2
import teacherPb_pb2 as teacherPb__pb2
import timePb_pb2 as timePb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='memberPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0ememberPb.proto\x1a\x0e\x65ntityPb.proto\x1a\rclassPb.proto\x1a\x0fteacherPb.proto\x1a\x0ctimePb.proto\"\x85\x01\n\x08MemberPb\x12\x19\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\t.EntityPb\x12\x1d\n\x08\x63lassRef\x18\x02 \x01(\x0b\x32\x0b.ClassPbRef\x12!\n\nteacherRef\x18\x03 \x03(\x0b\x32\r.TeacherPbRef\x12\x1c\n\x0b\x63reatedTime\x18\x06 \x01(\x0b\x32\x07.TimePbb\x06proto3'
  ,
  dependencies=[entityPb__pb2.DESCRIPTOR,classPb__pb2.DESCRIPTOR,teacherPb__pb2.DESCRIPTOR,timePb__pb2.DESCRIPTOR,])




_MEMBERPB = _descriptor.Descriptor(
  name='MemberPb',
  full_name='MemberPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='MemberPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classRef', full_name='MemberPb.classRef', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='teacherRef', full_name='MemberPb.teacherRef', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdTime', full_name='MemberPb.createdTime', index=3,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=81,
  serialized_end=214,
)

_MEMBERPB.fields_by_name['dbInfo'].message_type = entityPb__pb2._ENTITYPB
_MEMBERPB.fields_by_name['classRef'].message_type = classPb__pb2._CLASSPBREF
_MEMBERPB.fields_by_name['teacherRef'].message_type = teacherPb__pb2._TEACHERPBREF
_MEMBERPB.fields_by_name['createdTime'].message_type = timePb__pb2._TIMEPB
DESCRIPTOR.message_types_by_name['MemberPb'] = _MEMBERPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MemberPb = _reflection.GeneratedProtocolMessageType('MemberPb', (_message.Message,), {
  'DESCRIPTOR' : _MEMBERPB,
  '__module__' : 'memberPb_pb2'
  # @@protoc_insertion_point(class_scope:MemberPb)
  })
_sym_db.RegisterMessage(MemberPb)


# @@protoc_insertion_point(module_scope)
