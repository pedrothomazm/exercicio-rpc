from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stimulus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUTTON_CLICK: _ClassVar[Stimulus]
    FORM_SUMBISSION: _ClassVar[Stimulus]
    PAGE_LOAD: _ClassVar[Stimulus]
    DATA_ENTRY: _ClassVar[Stimulus]
    SYSTEM_BOOT: _ClassVar[Stimulus]
    FILE_UPLOAD: _ClassVar[Stimulus]
    DROPDOWN_SELECTION: _ClassVar[Stimulus]

class Target(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_INTERFACE: _ClassVar[Target]
    DATABASE_CONNECTOR: _ClassVar[Target]
    AUTHENTICATION_MODULE: _ClassVar[Target]
    DATA_PROCESSING_UNIT: _ClassVar[Target]
    NETWORK_ADAPTER: _ClassVar[Target]
    STORAGE_MANAGER: _ClassVar[Target]
    SECURITY_MODULE: _ClassVar[Target]
BUTTON_CLICK: Stimulus
FORM_SUMBISSION: Stimulus
PAGE_LOAD: Stimulus
DATA_ENTRY: Stimulus
SYSTEM_BOOT: Stimulus
FILE_UPLOAD: Stimulus
DROPDOWN_SELECTION: Stimulus
USER_INTERFACE: Target
DATABASE_CONNECTOR: Target
AUTHENTICATION_MODULE: Target
DATA_PROCESSING_UNIT: Target
NETWORK_ADAPTER: Target
STORAGE_MANAGER: Target
SECURITY_MODULE: Target

class Event(_message.Message):
    __slots__ = ("date", "user_id", "stimulus", "target")
    DATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STIMULUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    date: int
    user_id: int
    stimulus: Stimulus
    target: Target
    def __init__(self, date: _Optional[int] = ..., user_id: _Optional[int] = ..., stimulus: _Optional[_Union[Stimulus, str]] = ..., target: _Optional[_Union[Target, str]] = ...) -> None: ...

class EventList(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...
