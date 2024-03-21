from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SaeMessage(_message.Message):
    __slots__ = ("frame", "detections", "metrics")
    FRAME_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    frame: VideoFrame
    detections: _containers.RepeatedCompositeFieldContainer[Detection]
    metrics: Metrics
    def __init__(self, frame: _Optional[_Union[VideoFrame, _Mapping]] = ..., detections: _Optional[_Iterable[_Union[Detection, _Mapping]]] = ..., metrics: _Optional[_Union[Metrics, _Mapping]] = ...) -> None: ...

class VideoFrame(_message.Message):
    __slots__ = ("source_id", "timestamp_utc_ms", "shape", "frame_data", "frame_data_jpeg")
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_JPEG_FIELD_NUMBER: _ClassVar[int]
    source_id: str
    timestamp_utc_ms: int
    shape: Shape
    frame_data: bytes
    frame_data_jpeg: bytes
    def __init__(self, source_id: _Optional[str] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Union[Shape, _Mapping]] = ..., frame_data: _Optional[bytes] = ..., frame_data_jpeg: _Optional[bytes] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ("height", "width", "channels")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    channels: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class Detection(_message.Message):
    __slots__ = ("bounding_box", "confidence", "class_id", "object_id", "geo_coordinate")
    BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    bounding_box: BoundingBox
    confidence: float
    class_id: int
    object_id: bytes
    geo_coordinate: GeoCoordinate
    def __init__(self, bounding_box: _Optional[_Union[BoundingBox, _Mapping]] = ..., confidence: _Optional[float] = ..., class_id: _Optional[int] = ..., object_id: _Optional[bytes] = ..., geo_coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ...) -> None: ...

class BoundingBox(_message.Message):
    __slots__ = ("min_x", "min_y", "max_x", "max_y")
    MIN_X_FIELD_NUMBER: _ClassVar[int]
    MIN_Y_FIELD_NUMBER: _ClassVar[int]
    MAX_X_FIELD_NUMBER: _ClassVar[int]
    MAX_Y_FIELD_NUMBER: _ClassVar[int]
    min_x: float
    min_y: float
    max_x: float
    max_y: float
    def __init__(self, min_x: _Optional[float] = ..., min_y: _Optional[float] = ..., max_x: _Optional[float] = ..., max_y: _Optional[float] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class Metrics(_message.Message):
    __slots__ = ("detection_inference_time_us", "tracking_inference_time_us")
    DETECTION_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    TRACKING_INFERENCE_TIME_US_FIELD_NUMBER: _ClassVar[int]
    detection_inference_time_us: int
    tracking_inference_time_us: int
    def __init__(self, detection_inference_time_us: _Optional[int] = ..., tracking_inference_time_us: _Optional[int] = ...) -> None: ...
