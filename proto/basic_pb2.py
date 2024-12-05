# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basic.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basic.proto',
  package='osion.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x62\x61sic.proto\x12\x0bosion.proto\"\x13\n\x04\x42ool\x12\x0b\n\x03val\x18\x01 \x01(\x08\"\x12\n\x03Int\x12\x0b\n\x03val\x18\x01 \x01(\x05\"\x15\n\x06\x44ouble\x12\x0b\n\x03val\x18\x01 \x01(\x01\"\x15\n\x06String\x12\x0b\n\x03val\x18\x01 \x01(\tb\x06proto3'
)




_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='osion.proto.Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='osion.proto.Bool.val', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=47,
)


_INT = _descriptor.Descriptor(
  name='Int',
  full_name='osion.proto.Int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='osion.proto.Int.val', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=49,
  serialized_end=67,
)


_DOUBLE = _descriptor.Descriptor(
  name='Double',
  full_name='osion.proto.Double',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='osion.proto.Double.val', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=69,
  serialized_end=90,
)


_STRING = _descriptor.Descriptor(
  name='String',
  full_name='osion.proto.String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='osion.proto.String.val', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=92,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['Bool'] = _BOOL
DESCRIPTOR.message_types_by_name['Int'] = _INT
DESCRIPTOR.message_types_by_name['Double'] = _DOUBLE
DESCRIPTOR.message_types_by_name['String'] = _STRING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), {
  'DESCRIPTOR' : _BOOL,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:osion.proto.Bool)
  })
_sym_db.RegisterMessage(Bool)

Int = _reflection.GeneratedProtocolMessageType('Int', (_message.Message,), {
  'DESCRIPTOR' : _INT,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:osion.proto.Int)
  })
_sym_db.RegisterMessage(Int)

Double = _reflection.GeneratedProtocolMessageType('Double', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLE,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:osion.proto.Double)
  })
_sym_db.RegisterMessage(Double)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:osion.proto.String)
  })
_sym_db.RegisterMessage(String)


# @@protoc_insertion_point(module_scope)
