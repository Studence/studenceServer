# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entityPb_pb2 as entityPb__pb2
import namePb_pb2 as namePb__pb2
import timePb_pb2 as timePb__pb2
import classTypeUiPb_pb2 as classTypeUiPb__pb2
import schoolPb_pb2 as schoolPb__pb2
import sectionUiPb_pb2 as sectionUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='classPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rclassPb.proto\x1a\x0e\x65ntityPb.proto\x1a\x0cnamePb.proto\x1a\x0ctimePb.proto\x1a\x13\x63lassTypeUiPb.proto\x1a\x0eschoolPb.proto\x1a\x11sectionUiPb.proto\"\xd7\x01\n\x07\x43lassPb\x12\x19\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\t.EntityPb\x12\x15\n\x04name\x18\x02 \x01(\x0b\x32\x07.NamePb\x12!\n\tclassType\x18\x03 \x01(\x0e\x32\x0e.ClassTypeEnum\x12%\n\x0bsectionType\x18\x04 \x01(\x0e\x32\x10.SectionTypeEnum\x12\x1f\n\tschoolRef\x18\x05 \x01(\x0b\x32\x0c.SchoolPbRef\x12\x11\n\tclassCode\x18\x06 \x01(\t\x12\x1c\n\x0b\x63reatedTime\x18\x07 \x01(\x0b\x32\x07.TimePb\"\x96\x01\n\nClassPbRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\tschoolRef\x18\x02 \x01(\x0b\x32\x0c.SchoolPbRef\x12\x11\n\tclassCode\x18\x03 \x01(\t\x12!\n\tclassType\x18\x04 \x01(\x0e\x32\x0e.ClassTypeEnum\x12%\n\x0bsectionType\x18\x05 \x01(\x0e\x32\x10.SectionTypeEnumb\x06proto3'
  ,
  dependencies=[entityPb__pb2.DESCRIPTOR,namePb__pb2.DESCRIPTOR,timePb__pb2.DESCRIPTOR,classTypeUiPb__pb2.DESCRIPTOR,schoolPb__pb2.DESCRIPTOR,sectionUiPb__pb2.DESCRIPTOR,])




_CLASSPB = _descriptor.Descriptor(
  name='ClassPb',
  full_name='ClassPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='ClassPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ClassPb.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classType', full_name='ClassPb.classType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionType', full_name='ClassPb.sectionType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolRef', full_name='ClassPb.schoolRef', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classCode', full_name='ClassPb.classCode', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createdTime', full_name='ClassPb.createdTime', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=118,
  serialized_end=333,
)


_CLASSPBREF = _descriptor.Descriptor(
  name='ClassPbRef',
  full_name='ClassPbRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ClassPbRef.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schoolRef', full_name='ClassPbRef.schoolRef', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classCode', full_name='ClassPbRef.classCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classType', full_name='ClassPbRef.classType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionType', full_name='ClassPbRef.sectionType', index=4,
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
  serialized_start=336,
  serialized_end=486,
)

_CLASSPB.fields_by_name['dbInfo'].message_type = entityPb__pb2._ENTITYPB
_CLASSPB.fields_by_name['name'].message_type = namePb__pb2._NAMEPB
_CLASSPB.fields_by_name['classType'].enum_type = classTypeUiPb__pb2._CLASSTYPEENUM
_CLASSPB.fields_by_name['sectionType'].enum_type = sectionUiPb__pb2._SECTIONTYPEENUM
_CLASSPB.fields_by_name['schoolRef'].message_type = schoolPb__pb2._SCHOOLPBREF
_CLASSPB.fields_by_name['createdTime'].message_type = timePb__pb2._TIMEPB
_CLASSPBREF.fields_by_name['schoolRef'].message_type = schoolPb__pb2._SCHOOLPBREF
_CLASSPBREF.fields_by_name['classType'].enum_type = classTypeUiPb__pb2._CLASSTYPEENUM
_CLASSPBREF.fields_by_name['sectionType'].enum_type = sectionUiPb__pb2._SECTIONTYPEENUM
DESCRIPTOR.message_types_by_name['ClassPb'] = _CLASSPB
DESCRIPTOR.message_types_by_name['ClassPbRef'] = _CLASSPBREF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassPb = _reflection.GeneratedProtocolMessageType('ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _CLASSPB,
  '__module__' : 'classPb_pb2'
  # @@protoc_insertion_point(class_scope:ClassPb)
  })
_sym_db.RegisterMessage(ClassPb)

ClassPbRef = _reflection.GeneratedProtocolMessageType('ClassPbRef', (_message.Message,), {
  'DESCRIPTOR' : _CLASSPBREF,
  '__module__' : 'classPb_pb2'
  # @@protoc_insertion_point(class_scope:ClassPbRef)
  })
_sym_db.RegisterMessage(ClassPbRef)


# @@protoc_insertion_point(module_scope)
