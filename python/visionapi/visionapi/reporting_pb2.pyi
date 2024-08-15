from visionapi import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IncidentMessage(_message.Message):
    __slots__ = ("timestamp_utc_ms", "media_url", "model_info")
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_URL_FIELD_NUMBER: _ClassVar[int]
    MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
    timestamp_utc_ms: int
    media_url: str
    model_info: _common_pb2.ModelInfo
    def __init__(self, timestamp_utc_ms: _Optional[int] = ..., media_url: _Optional[str] = ..., model_info: _Optional[_Union[_common_pb2.ModelInfo, _Mapping]] = ...) -> None: ...
