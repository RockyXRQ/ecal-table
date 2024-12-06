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
  package='et.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x62\x61sic.proto\x12\x08\x65t.proto\"\x13\n\x04\x42ool\x12\x0b\n\x03val\x18\x01 \x01(\x08\"\x12\n\x03Int\x12\x0b\n\x03val\x18\x01 \x01(\x05\"\x15\n\x06\x44ouble\x12\x0b\n\x03val\x18\x01 \x01(\x01\"\x12\n\x03Str\x12\x0b\n\x03val\x18\x01 \x01(\tb\x06proto3'
)




_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='et.proto.Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='et.proto.Bool.val', index=0,
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
  serialized_start=25,
  serialized_end=44,
)


_INT = _descriptor.Descriptor(
  name='Int',
  full_name='et.proto.Int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='et.proto.Int.val', index=0,
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
  serialized_start=46,
  serialized_end=64,
)


_DOUBLE = _descriptor.Descriptor(
  name='Double',
  full_name='et.proto.Double',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='et.proto.Double.val', index=0,
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
  serialized_start=66,
  serialized_end=87,
)


_STR = _descriptor.Descriptor(
  name='Str',
  full_name='et.proto.Str',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='et.proto.Str.val', index=0,
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
  serialized_start=89,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Bool'] = _BOOL
DESCRIPTOR.message_types_by_name['Int'] = _INT
DESCRIPTOR.message_types_by_name['Double'] = _DOUBLE
DESCRIPTOR.message_types_by_name['Str'] = _STR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), {
  'DESCRIPTOR' : _BOOL,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:et.proto.Bool)
  })
_sym_db.RegisterMessage(Bool)

Int = _reflection.GeneratedProtocolMessageType('Int', (_message.Message,), {
  'DESCRIPTOR' : _INT,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:et.proto.Int)
  })
_sym_db.RegisterMessage(Int)

Double = _reflection.GeneratedProtocolMessageType('Double', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLE,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:et.proto.Double)
  })
_sym_db.RegisterMessage(Double)

Str = _reflection.GeneratedProtocolMessageType('Str', (_message.Message,), {
  'DESCRIPTOR' : _STR,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:et.proto.Str)
  })
_sym_db.RegisterMessage(Str)


# @@protoc_insertion_point(module_scope)