# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: visionapi/messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18visionapi/messages.proto\x12\tvisionapi\"n\n\nVideoFrame\x12\x11\n\tsource_id\x18\x01 \x01(\x0c\x12\x18\n\x10timestamp_utc_ms\x18\x02 \x01(\x04\x12\x1f\n\x05shape\x18\x03 \x01(\x0b\x32\x10.visionapi.Shape\x12\x12\n\nframe_data\x18\x04 \x01(\x0c\"8\n\x05Shape\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x10\n\x08\x63hannels\x18\x03 \x01(\r\"\x86\x01\n\x0f\x44\x65tectionOutput\x12$\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x15.visionapi.VideoFrame\x12(\n\ndetections\x18\x02 \x03(\x0b\x32\x14.visionapi.Detection\x12#\n\x07metrics\x18\x63 \x01(\x0b\x32\x12.visionapi.Metrics\"_\n\tDetection\x12,\n\x0c\x62ounding_box\x18\x01 \x01(\x0b\x32\x16.visionapi.BoundingBox\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x10\n\x08\x63lass_id\x18\x03 \x01(\r\"I\n\x0b\x42oundingBox\x12\r\n\x05min_x\x18\x01 \x01(\r\x12\r\n\x05min_y\x18\x02 \x01(\r\x12\r\n\x05max_x\x18\x03 \x01(\r\x12\r\n\x05max_y\x18\x04 \x01(\r\"\x94\x01\n\x0eTrackingOutput\x12$\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x15.visionapi.VideoFrame\x12\x37\n\x12tracked_detections\x18\x02 \x03(\x0b\x32\x1b.visionapi.TrackedDetection\x12#\n\x07metrics\x18\x63 \x01(\x0b\x32\x12.visionapi.Metrics\"N\n\x10TrackedDetection\x12\'\n\tdetection\x18\x01 \x01(\x0b\x32\x14.visionapi.Detection\x12\x11\n\tobject_id\x18\x02 \x01(\x0c\"R\n\x07Metrics\x12#\n\x1b\x64\x65tection_inference_time_us\x18\x01 \x01(\r\x12\"\n\x1atracking_inference_time_us\x18\x02 \x01(\rB\x16\n\x14\x64\x65.starwit.visionapib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'visionapi.messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024de.starwit.visionapi'
  _globals['_VIDEOFRAME']._serialized_start=39
  _globals['_VIDEOFRAME']._serialized_end=149
  _globals['_SHAPE']._serialized_start=151
  _globals['_SHAPE']._serialized_end=207
  _globals['_DETECTIONOUTPUT']._serialized_start=210
  _globals['_DETECTIONOUTPUT']._serialized_end=344
  _globals['_DETECTION']._serialized_start=346
  _globals['_DETECTION']._serialized_end=441
  _globals['_BOUNDINGBOX']._serialized_start=443
  _globals['_BOUNDINGBOX']._serialized_end=516
  _globals['_TRACKINGOUTPUT']._serialized_start=519
  _globals['_TRACKINGOUTPUT']._serialized_end=667
  _globals['_TRACKEDDETECTION']._serialized_start=669
  _globals['_TRACKEDDETECTION']._serialized_end=747
  _globals['_METRICS']._serialized_start=749
  _globals['_METRICS']._serialized_end=831
# @@protoc_insertion_point(module_scope)
