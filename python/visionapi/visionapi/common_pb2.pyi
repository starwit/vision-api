from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[MessageType]
    SAE: _ClassVar[MessageType]
    DETECTION_COUNT: _ClassVar[MessageType]
    POSITION: _ClassVar[MessageType]
    ANOMALY: _ClassVar[MessageType]
    INCIDENT: _ClassVar[MessageType]
UNSPECIFIED: MessageType
SAE: MessageType
DETECTION_COUNT: MessageType
POSITION: MessageType
ANOMALY: MessageType
INCIDENT: MessageType

class ModelInfo(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class TypeMessage(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: MessageType
    def __init__(self, type: _Optional[_Union[MessageType, str]] = ...) -> None: ...
