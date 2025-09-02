from visionapi import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectionCountMessage(_message.Message):
    __slots__ = ("timestamp_utc_ms", "detection_counts", "sae_uuid", "type")
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_COUNTS_FIELD_NUMBER: _ClassVar[int]
    SAE_UUID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    timestamp_utc_ms: int
    detection_counts: _containers.RepeatedCompositeFieldContainer[DetectionCount]
    sae_uuid: bytes
    type: _common_pb2.MessageType
    def __init__(self, timestamp_utc_ms: _Optional[int] = ..., detection_counts: _Optional[_Iterable[_Union[DetectionCount, _Mapping]]] = ..., sae_uuid: _Optional[bytes] = ..., type: _Optional[_Union[_common_pb2.MessageType, str]] = ...) -> None: ...

class DetectionCount(_message.Message):
    __slots__ = ("class_id", "class_name", "count", "location")
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    class_id: int
    class_name: str
    count: int
    location: _common_pb2.GeoCoordinate
    def __init__(self, class_id: _Optional[int] = ..., class_name: _Optional[str] = ..., count: _Optional[int] = ..., location: _Optional[_Union[_common_pb2.GeoCoordinate, _Mapping]] = ...) -> None: ...
