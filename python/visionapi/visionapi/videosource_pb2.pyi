from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFrame(_message.Message):
    __slots__ = ["source_id", "timestamp_utc_ms", "shape", "frame_data"]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    source_id: bytes
    timestamp_utc_ms: int
    shape: _containers.RepeatedScalarFieldContainer[int]
    frame_data: bytes
    def __init__(self, source_id: _Optional[bytes] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Iterable[int]] = ..., frame_data: _Optional[bytes] = ...) -> None: ...
