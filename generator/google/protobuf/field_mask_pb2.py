# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/field_mask.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/field_mask.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_pb=_b('\n google/protobuf/field_mask.proto\x12\x0fgoogle.protobuf\"\x1a\n\tFieldMask\x12\r\n\x05paths\x18\x01 \x03(\tBQ\n\x13\x63om.google.protobufB\x0e\x46ieldMaskProtoP\x01\xa0\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FIELDMASK = _descriptor.Descriptor(
  name='FieldMask',
  full_name='google.protobuf.FieldMask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='google.protobuf.FieldMask.paths', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['FieldMask'] = _FIELDMASK

FieldMask = _reflection.GeneratedProtocolMessageType('FieldMask', (_message.Message,), dict(
  DESCRIPTOR = _FIELDMASK,
  __module__ = 'google.protobuf.field_mask_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.FieldMask)
  ))
_sym_db.RegisterMessage(FieldMask)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.google.protobufB\016FieldMaskProtoP\001\240\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'))
# @@protoc_insertion_point(module_scope)
