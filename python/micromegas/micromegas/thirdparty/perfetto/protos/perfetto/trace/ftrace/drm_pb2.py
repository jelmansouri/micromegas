# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/perfetto/trace/ftrace/drm.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'protos/perfetto/trace/ftrace/drm.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&protos/perfetto/trace/ftrace/drm.proto\x12\x0fperfetto.protos\"W\n\x19\x44rmVblankEventFtraceEvent\x12\x0c\n\x04\x63rtc\x18\x01 \x01(\x05\x12\x11\n\thigh_prec\x18\x02 \x01(\r\x12\x0b\n\x03seq\x18\x03 \x01(\r\x12\x0c\n\x04time\x18\x04 \x01(\x03\"M\n\"DrmVblankEventDeliveredFtraceEvent\x12\x0c\n\x04\x63rtc\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ile\x18\x02 \x01(\x04\x12\x0b\n\x03seq\x18\x03 \x01(\r')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.ftrace.drm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DRMVBLANKEVENTFTRACEEVENT']._serialized_start=59
  _globals['_DRMVBLANKEVENTFTRACEEVENT']._serialized_end=146
  _globals['_DRMVBLANKEVENTDELIVEREDFTRACEEVENT']._serialized_start=148
  _globals['_DRMVBLANKEVENTDELIVEREDFTRACEEVENT']._serialized_end=225
# @@protoc_insertion_point(module_scope)