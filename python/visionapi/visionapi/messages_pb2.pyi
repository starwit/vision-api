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
    source_id: str
    timestamp_utc_ms: int
    shape: Shape
    frame_data: bytes
    def __init__(self, source_id: _Optional[str] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Union[Shape, _Mapping]] = ..., frame_data: _Optional[bytes] = ...) -> None: ...

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
    __slots__ = ["frame", "detections", "metrics"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    frame: VideoFrame
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    metrics: Metrics
    def __init__(self, frame: _Optional[_Union[VideoFrame, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ..., metrics: _Optional[_Union[Metrics, _Mapping]] = ...) -> None: ...

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

class TrackingOutput(_message.Message):
    __slots__ = ["frame", "tracked_detections", "metrics"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    TRACKED_DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    frame: VideoFrame
    tracked_detections: _containers.RepeatedCompositeFieldContainer[TrackedDetection]
    metrics: Metrics
    def __init__(self, frame: _Optional[_Union[VideoFrame, _Mapping]] = ..., tracked_detections: _Optional[_Iterable[_Union[TrackedDetection, _Mapping]]] = ..., metrics: _Optional[_Union[Metrics, _Mapping]] = ...) -> None: ...

class TrackedDetection(_message.Message):
    __slots__ = ["detection", "object_id"]
    DETECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    detection: Detection
    object_id: bytes
    def __init__(self, detection: _Optional[_Union[Detection, _Mapping]] = ..., object_id: _Optional[bytes] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ["detection_inference_time_us", "tracking_inference_time_us"]
    DETECTION_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    TRACKING_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    detection_inference_time_us: int
    tracking_inference_time_us: int
    def __init__(self, detection_inference_time_us: _Optional[int] = ..., tracking_inference_time_us: _Optional[int] = ...) -> None: ...
