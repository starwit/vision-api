from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFrame(_message.Message):
    __slots__ = ["timestamp_utc_ms", "shape", "frame"]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    timestamp_utc_ms: int
    shape: _containers.RepeatedScalarFieldContainer[int]
    frame: bytes
    def __init__(self, timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Iterable[int]] = ..., frame: _Optional[bytes] = ...) -> None: ...
