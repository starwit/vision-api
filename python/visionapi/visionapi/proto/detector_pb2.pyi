from proto import videosource_pb2 as _videosource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectionOutput(_message.Message):
    __slots__ = ["frame", "detections"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    frame: _videosource_pb2.VideoFrame
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    def __init__(self, frame: _Optional[_Union[_videosource_pb2.VideoFrame, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ...) -> None: ...

class Detection(_message.Message):
    __slots__ = ["bounding_box", "confidence", "class_id"]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    bounding_box: BoundingBox
    confidence: float
    class_id: int
    def __init__(self, bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., confidence: _Optional[float] = ..., class_id: _Optional[int] = ...) -> None: ...

class BoundingBox(_message.Message):
    __slots__ = ["min_x", "min_y", "max_x", "max_y"]
    MIN_X_FIELD_NUMBER: _ClassVar[int]
    MIN_Y_FIELD_NUMBER: _ClassVar[int]
    MAX_X_FIELD_NUMBER: _ClassVar[int]
    MAX_Y_FIELD_NUMBER: _ClassVar[int]
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    def __init__(self, min_x: _Optional[int] = ..., min_y: _Optional[int] = ..., max_x: _Optional[int] = ..., max_y: _Optional[int] = ...) -> None: ...
