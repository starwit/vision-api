import videosource_pb2 as _videosource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Detections(_message.Message):
    __slots__ = ["frame"]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    frame: _videosource_pb2.VideoFrame
    def __init__(self, frame: _Optional[_Union[_videosource_pb2.VideoFrame, _Mapping]] = ...) -> None: ...
