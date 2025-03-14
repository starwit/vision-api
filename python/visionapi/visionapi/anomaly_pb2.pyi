from visionapi import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnomalyMessage(_message.Message):
    __slots__ = ("jpeg_frames", "trajectories", "model_info", "camera_location", "source_id")
    JPEG_FRAMES_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORIES_FIELD_NUMBER: _ClassVar[int]
    MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    jpeg_frames: _containers.RepeatedCompositeFieldContainer[JpegFrame]
    trajectories: _containers.RepeatedCompositeFieldContainer[Trajectory]
    model_info: _common_pb2.ModelInfo
    camera_location: _common_pb2.GeoCoordinate
    source_id: str
    def __init__(self, jpeg_frames: _Optional[_Iterable[_Union[JpegFrame, _Mapping]]] = ..., trajectories: _Optional[_Iterable[_Union[Trajectory, _Mapping]]] = ..., model_info: _Optional[_Union[_common_pb2.ModelInfo, _Mapping]] = ..., camera_location: _Optional[_Union[_common_pb2.GeoCoordinate, _Mapping]] = ..., source_id: _Optional[str] = ...) -> None: ...

class JpegFrame(_message.Message):
    __slots__ = ("timestamp_utc_ms", "frame_data_jpeg")
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_JPEG_FIELD_NUMBER: _ClassVar[int]
    timestamp_utc_ms: int
    frame_data_jpeg: bytes
    def __init__(self, timestamp_utc_ms: _Optional[int] = ..., frame_data_jpeg: _Optional[bytes] = ...) -> None: ...

class Trajectory(_message.Message):
    __slots__ = ("trajectory_points", "class_id", "object_id")
    TRAJECTORY_POINTS_FIELD_NUMBER: _ClassVar[int]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    trajectory_points: _containers.RepeatedCompositeFieldContainer[TrajectoryPoint]
    class_id: int
    object_id: bytes
    def __init__(self, trajectory_points: _Optional[_Iterable[_Union[TrajectoryPoint, _Mapping]]] = ..., class_id: _Optional[int] = ..., object_id: _Optional[bytes] = ...) -> None: ...

class TrajectoryPoint(_message.Message):
    __slots__ = ("timestamp_utc_ms", "geo_coordinate", "detection_center", "anomaly_trigger")
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_CENTER_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    timestamp_utc_ms: int
    geo_coordinate: _common_pb2.GeoCoordinate
    detection_center: Point
    anomaly_trigger: bool
    def __init__(self, timestamp_utc_ms: _Optional[int] = ..., geo_coordinate: _Optional[_Union[_common_pb2.GeoCoordinate, _Mapping]] = ..., detection_center: _Optional[_Union[Point, _Mapping]] = ..., anomaly_trigger: bool = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...
