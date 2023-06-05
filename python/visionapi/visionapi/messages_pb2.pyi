from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFrame(_message.Message):
    __slots__ = ["source_id", "timestamp_utc_ms", "shape", "frame_data"]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    source_id: bytes
    timestamp_utc_ms: int
    shape: Shape
    frame_data: bytes
    def __init__(self, source_id: _Optional[bytes] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Union[Shape, _Mapping]] = ..., frame_data: _Optional[bytes] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ["height", "width", "channels"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    channels: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class DetectionOutput(_message.Message):
    __slots__ = ["frame", "detections"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    frame: VideoFrame
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    def __init__(self, frame: _Optional[_Union[VideoFrame, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ...) -> None: ...

class Detection(_message.Message):
    __slots__ = ["bounding_box", "confidence", "class_id", "inference_time_ms"]
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    bounding_box: BoundingBox
    confidence: float
    class_id: int
    inference_time_ms: int
    def __init__(self, bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., confidence: _Optional[float] = ..., class_id: _Optional[int] = ..., inference_time_ms: _Optional[int] = ...) -> None: ...

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

class TrackingOutput(_message.Message):
    __slots__ = ["frame", "tracked_detections"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    TRACKED_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    frame: VideoFrame
    tracked_detections: _containers.RepeatedCompositeFieldContainer[TrackedDetection]
    def __init__(self, frame: _Optional[_Union[VideoFrame, _Mapping]] = ..., tracked_detections: _Optional[_Iterable[_Union[TrackedDetection, _Mapping]]] = ...) -> None: ...

class TrackedDetection(_message.Message):
    __slots__ = ["detection", "object_id", "inference_time_ms"]
    DETECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    detection: Detection
    object_id: bytes
    inference_time_ms: int
    def __init__(self, detection: _Optional[_Union[Detection, _Mapping]] = ..., object_id: _Optional[bytes] = ..., inference_time_ms: _Optional[int] = ...) -> None: ...