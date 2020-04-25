# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: studentPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entityPb_pb2 as entityPb__pb2
import namePb_pb2 as namePb__pb2
import emailPb_pb2 as emailPb__pb2
import addressPb_pb2 as addressPb__pb2
import timePb_pb2 as timePb__pb2
import mobilePb_pb2 as mobilePb__pb2
import classPb_pb2 as classPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='studentPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0fstudentPb.proto\x1a\x0e\x65ntityPb.proto\x1a\x0cnamePb.proto\x1a\remailPb.proto\x1a\x0f\x61\x64\x64ressPb.proto\x1a\x0ctimePb.proto\x1a\x0emobilePb.proto\x1a\rclassPb.proto\"\xe0\x01\n\tStudentPb\x12\x19\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\t.EntityPb\x12\x15\n\x04name\x18\x02 \x01(\x0b\x32\x07.NamePb\x12\x17\n\x05\x65mail\x18\x03 \x01(\x0b\x32\x08.EmailPb\x12\x1b\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\n.AddressPb\x12\x19\n\x06mobile\x18\x05 \x03(\x0b\x32\t.MobilePb\x12\x1c\n\x0b\x63reatedTime\x18\x06 \x01(\x0b\x32\x07.TimePb\x12\x1d\n\x08\x63lassRef\x18\x07 \x01(\x0b\x32\x0b.ClassPbRef\x12\x13\n\x0bstudentCode\x18\x08 \x01(\tb\x06proto3'
  ,
  dependencies=[entityPb__pb2.DESCRIPTOR,namePb__pb2.DESCRIPTOR,emailPb__pb2.DESCRIPTOR,addressPb__pb2.DESCRIPTOR,timePb__pb2.DESCRIPTOR,mobilePb__pb2.DESCRIPTOR,classPb__pb2.DESCRIPTOR,])




_STUDENTPB = _descriptor.Descriptor(
  name='StudentPb',
  full_name='StudentPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='StudentPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='StudentPb.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='StudentPb.email', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='StudentPb.address', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='StudentPb.mobile', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdTime', full_name='StudentPb.createdTime', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classRef', full_name='StudentPb.classRef', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='studentCode', full_name='StudentPb.studentCode', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=127,
  serialized_end=351,
)

_STUDENTPB.fields_by_name['dbInfo'].message_type = entityPb__pb2._ENTITYPB
_STUDENTPB.fields_by_name['name'].message_type = namePb__pb2._NAMEPB
_STUDENTPB.fields_by_name['email'].message_type = emailPb__pb2._EMAILPB
_STUDENTPB.fields_by_name['address'].message_type = addressPb__pb2._ADDRESSPB
_STUDENTPB.fields_by_name['mobile'].message_type = mobilePb__pb2._MOBILEPB
_STUDENTPB.fields_by_name['createdTime'].message_type = timePb__pb2._TIMEPB
_STUDENTPB.fields_by_name['classRef'].message_type = classPb__pb2._CLASSPBREF
DESCRIPTOR.message_types_by_name['StudentPb'] = _STUDENTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StudentPb = _reflection.GeneratedProtocolMessageType('StudentPb', (_message.Message,), {
  'DESCRIPTOR' : _STUDENTPB,
  '__module__' : 'studentPb_pb2'
  # @@protoc_insertion_point(class_scope:StudentPb)
  })
_sym_db.RegisterMessage(StudentPb)


# @@protoc_insertion_point(module_scope)