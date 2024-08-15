# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visionapi/sae.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from visionapi import common_pb2 as visionapi_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13visionapi/sae.proto\x12\tvisionapi\x1a\x16visionapi/common.proto\"\x81\x01\n\nSaeMessage\x12$\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x15.visionapi.VideoFrame\x12(\n\ndetections\x18\x02 \x03(\x0b\x32\x14.visionapi.Detection\x12#\n\x07metrics\x18\x63 \x01(\x0b\x32\x12.visionapi.Metrics\"\x87\x01\n\nVideoFrame\x12\x11\n\tsource_id\x18\x01 \x01(\t\x12\x18\n\x10timestamp_utc_ms\x18\x02 \x01(\x04\x12\x1f\n\x05shape\x18\x03 \x01(\x0b\x32\x10.visionapi.Shape\x12\x12\n\nframe_data\x18\x04 \x01(\x0c\x12\x17\n\x0f\x66rame_data_jpeg\x18\x05 \x01(\x0c\"8\n\x05Shape\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x10\n\x08\x63hannels\x18\x03 \x01(\r\"\xa4\x01\n\tDetection\x12,\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x16.visionapi.BoundingBox\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x10\n\x08\x63lass_id\x18\x03 \x01(\r\x12\x11\n\tobject_id\x18\x04 \x01(\x0c\x12\x30\n\x0egeo_coordinate\x18\x05 \x01(\x0b\x32\x18.visionapi.GeoCoordinate\"I\n\x0b\x42oundingBox\x12\r\n\x05min_x\x18\x01 \x01(\x02\x12\r\n\x05min_y\x18\x02 \x01(\x02\x12\r\n\x05max_x\x18\x03 \x01(\x02\x12\r\n\x05max_y\x18\x04 \x01(\x02\"R\n\x07Metrics\x12#\n\x1b\x64\x65tection_inference_time_us\x18\x01 \x01(\r\x12\"\n\x1atracking_inference_time_us\x18\x02 \x01(\rB\x16\n\x14\x64\x65.starwit.visionapib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visionapi.sae_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024de.starwit.visionapi'
  _globals['_SAEMESSAGE']._serialized_start=59
  _globals['_SAEMESSAGE']._serialized_end=188
  _globals['_VIDEOFRAME']._serialized_start=191
  _globals['_VIDEOFRAME']._serialized_end=326
  _globals['_SHAPE']._serialized_start=328
  _globals['_SHAPE']._serialized_end=384
  _globals['_DETECTION']._serialized_start=387
  _globals['_DETECTION']._serialized_end=551
  _globals['_BOUNDINGBOX']._serialized_start=553
  _globals['_BOUNDINGBOX']._serialized_end=626
  _globals['_METRICS']._serialized_start=628
  _globals['_METRICS']._serialized_end=710
# @@protoc_insertion_point(module_scope)
