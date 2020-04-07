# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: organisationUiPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nameUiPb_pb2 as nameUiPb__pb2
import entityUiPb_pb2 as entityUiPb__pb2
import timeUiPb_pb2 as timeUiPb__pb2
import summaryUiPb_pb2 as summaryUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='organisationUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16organisationUiPb.proto\x1a\x0enameUiPb.proto\x1a\x10\x65ntityUiPb.proto\x1a\x0etimeUiPb.proto\x1a\x11summaryUiPb.proto\"a\n\x10OrganisationUiPb\x12\x1b\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\x0b.EntityUiPb\x12\x17\n\x04name\x18\x02 \x01(\x0b\x32\t.NameUiPb\x12\x17\n\x04time\x18\x03 \x01(\x0b\x32\t.TimeUiPb\"\x1f\n\x1dOrganisationSearchRequestUiPb\"c\n\x1eOrganisationSearchResponseUiPb\x12\x1d\n\x07summary\x18\x01 \x01(\x0b\x32\x0c.SummaryUiPb\x12\"\n\x07results\x18\x02 \x03(\x0b\x32\x11.OrganisationUiPbb\x06proto3'
  ,
  dependencies=[nameUiPb__pb2.DESCRIPTOR,entityUiPb__pb2.DESCRIPTOR,timeUiPb__pb2.DESCRIPTOR,summaryUiPb__pb2.DESCRIPTOR,])




_ORGANISATIONUIPB = _descriptor.Descriptor(
  name='OrganisationUiPb',
  full_name='OrganisationUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='OrganisationUiPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='OrganisationUiPb.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='OrganisationUiPb.time', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=95,
  serialized_end=192,
)


_ORGANISATIONSEARCHREQUESTUIPB = _descriptor.Descriptor(
  name='OrganisationSearchRequestUiPb',
  full_name='OrganisationSearchRequestUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=194,
  serialized_end=225,
)


_ORGANISATIONSEARCHRESPONSEUIPB = _descriptor.Descriptor(
  name='OrganisationSearchResponseUiPb',
  full_name='OrganisationSearchResponseUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='OrganisationSearchResponseUiPb.summary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='OrganisationSearchResponseUiPb.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=227,
  serialized_end=326,
)

_ORGANISATIONUIPB.fields_by_name['dbInfo'].message_type = entityUiPb__pb2._ENTITYUIPB
_ORGANISATIONUIPB.fields_by_name['name'].message_type = nameUiPb__pb2._NAMEUIPB
_ORGANISATIONUIPB.fields_by_name['time'].message_type = timeUiPb__pb2._TIMEUIPB
_ORGANISATIONSEARCHRESPONSEUIPB.fields_by_name['summary'].message_type = summaryUiPb__pb2._SUMMARYUIPB
_ORGANISATIONSEARCHRESPONSEUIPB.fields_by_name['results'].message_type = _ORGANISATIONUIPB
DESCRIPTOR.message_types_by_name['OrganisationUiPb'] = _ORGANISATIONUIPB
DESCRIPTOR.message_types_by_name['OrganisationSearchRequestUiPb'] = _ORGANISATIONSEARCHREQUESTUIPB
DESCRIPTOR.message_types_by_name['OrganisationSearchResponseUiPb'] = _ORGANISATIONSEARCHRESPONSEUIPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrganisationUiPb = _reflection.GeneratedProtocolMessageType('OrganisationUiPb', (_message.Message,), {
  'DESCRIPTOR' : _ORGANISATIONUIPB,
  '__module__' : 'organisationUiPb_pb2'
  # @@protoc_insertion_point(class_scope:OrganisationUiPb)
  })
_sym_db.RegisterMessage(OrganisationUiPb)

OrganisationSearchRequestUiPb = _reflection.GeneratedProtocolMessageType('OrganisationSearchRequestUiPb', (_message.Message,), {
  'DESCRIPTOR' : _ORGANISATIONSEARCHREQUESTUIPB,
  '__module__' : 'organisationUiPb_pb2'
  # @@protoc_insertion_point(class_scope:OrganisationSearchRequestUiPb)
  })
_sym_db.RegisterMessage(OrganisationSearchRequestUiPb)

OrganisationSearchResponseUiPb = _reflection.GeneratedProtocolMessageType('OrganisationSearchResponseUiPb', (_message.Message,), {
  'DESCRIPTOR' : _ORGANISATIONSEARCHRESPONSEUIPB,
  '__module__' : 'organisationUiPb_pb2'
  # @@protoc_insertion_point(class_scope:OrganisationSearchResponseUiPb)
  })
_sym_db.RegisterMessage(OrganisationSearchResponseUiPb)


# @@protoc_insertion_point(module_scope)