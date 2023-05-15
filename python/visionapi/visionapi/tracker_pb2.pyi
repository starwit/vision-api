from visionapi import detector_pb2 as _detector_pb2
from visionapi import videosource_pb2 as _videosource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrackingOutput(_message.Message):
    __slots__ = ["frame", "tracked_detections"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    TRACKED_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    frame: _videosource_pb2.VideoFrame
    tracked_detections: _containers.RepeatedCompositeFieldContainer[TrackedDetection]
    def __init__(self, frame: _Optional[_Union[_videosource_pb2.VideoFrame, _Mapping]] = ..., tracked_detections: _Optional[_Iterable[_Union[TrackedDetection, _Mapping]]] = ...) -> None: ...

class TrackedDetection(_message.Message):
    __slots__ = ["detection", "object_id"]
    DETECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    detection: _detector_pb2.Detection
    object_id: bytes
    def __init__(self, detection: _Optional[_Union[_detector_pb2.Detection, _Mapping]] = ..., object_id: _Optional[bytes] = ...) -> None: ...
