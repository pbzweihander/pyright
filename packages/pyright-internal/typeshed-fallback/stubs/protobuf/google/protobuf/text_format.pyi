import sys
from _typeshed import SupportsWrite
from typing import Any, Callable, Iterable, Optional, Text, Tuple, TypeVar

from .descriptor import FieldDescriptor
from .descriptor_pool import DescriptorPool
from .message import Message

if sys.version_info < (3, 0):
    long = int

_M = TypeVar("_M", bound=Message)  # message type (of self)

class Error(Exception): ...

class ParseError(Error):
    def __init__(self, message: Optional[str] = ..., line: Optional[int] = ..., column: Optional[int] = ...) -> None: ...
    def GetLine(self) -> Optional[int]: ...
    def GetColumn(self) -> Optional[int]: ...

class TextWriter:
    def __init__(self, as_utf8: bool) -> None: ...
    def write(self, val: Text) -> int: ...
    def getvalue(self) -> str: ...
    def close(self) -> None: ...

_MessageFormatter = Callable[[Message, int, bool], Optional[Text]]

def MessageToString(
    message: Message,
    as_utf8: bool = ...,
    as_one_line: bool = ...,
    use_short_repeated_primitives: bool = ...,
    pointy_brackets: bool = ...,
    use_index_order: bool = ...,
    float_format: Optional[str] = ...,
    double_format: Optional[str] = ...,
    use_field_number: bool = ...,
    descriptor_pool: Optional[DescriptorPool] = ...,
    indent: int = ...,
    message_formatter: Optional[_MessageFormatter] = ...,
    print_unknown_fields: bool = ...,
    force_colon: bool = ...,
) -> str: ...
def MessageToBytes(
    message: Message,
    as_utf8: bool = ...,
    as_one_line: bool = ...,
    use_short_repeated_primitives: bool = ...,
    pointy_brackets: bool = ...,
    use_index_order: bool = ...,
    float_format: Optional[str] = ...,
    double_format: Optional[str] = ...,
    use_field_number: bool = ...,
    descriptor_pool: Optional[DescriptorPool] = ...,
    indent: int = ...,
    message_formatter: _MessageFormatter = ...,
    print_unknown_fields: bool = ...,
    force_colon: bool = ...,
) -> bytes: ...
def PrintMessage(
    message: Message,
    out: SupportsWrite[str],
    indent: int = ...,
    as_utf8: bool = ...,
    as_one_line: bool = ...,
    use_short_repeated_primitives: bool = ...,
    pointy_brackets: bool = ...,
    use_index_order: bool = ...,
    float_format: Optional[str] = ...,
    double_format: Optional[str] = ...,
    use_field_number: bool = ...,
    descriptor_pool: Optional[DescriptorPool] = ...,
    message_formatter: Optional[_MessageFormatter] = ...,
    print_unknown_fields: bool = ...,
    force_colon: bool = ...,
) -> None: ...
def PrintField(
    field: FieldDescriptor,
    value: Any,
    out: SupportsWrite[str],
    indent: int = ...,
    as_utf8: bool = ...,
    as_one_line: bool = ...,
    use_short_repeated_primitives: bool = ...,
    pointy_brackets: bool = ...,
    use_index_order: bool = ...,
    float_format: Optional[str] = ...,
    double_format: Optional[str] = ...,
    message_formatter: Optional[_MessageFormatter] = ...,
    print_unknown_fields: bool = ...,
    force_colon: bool = ...,
) -> None: ...
def PrintFieldValue(
    field: FieldDescriptor,
    value: Any,
    out: SupportsWrite[str],
    indent: int = ...,
    as_utf8: bool = ...,
    as_one_line: bool = ...,
    use_short_repeated_primitives: bool = ...,
    pointy_brackets: bool = ...,
    use_index_order: bool = ...,
    float_format: Optional[str] = ...,
    double_format: Optional[str] = ...,
    message_formatter: Optional[_MessageFormatter] = ...,
    print_unknown_fields: bool = ...,
    force_colon: bool = ...,
) -> None: ...

class _Printer:
    out: SupportsWrite[str] = ...
    indent: int = ...
    as_utf8: bool = ...
    as_one_line: bool = ...
    use_short_repeated_primitives: bool = ...
    pointy_brackets: bool = ...
    use_index_order: bool = ...
    float_format: Optional[str] = ...
    double_format: Optional[str] = ...
    use_field_number: bool = ...
    descriptor_pool: Optional[DescriptorPool] = ...
    message_formatter: Optional[_MessageFormatter] = ...
    print_unknown_fields: bool = ...
    force_colon: bool = ...
    def __init__(
        self,
        out: SupportsWrite[str],
        indent: int = ...,
        as_utf8: bool = ...,
        as_one_line: bool = ...,
        use_short_repeated_primitives: bool = ...,
        pointy_brackets: bool = ...,
        use_index_order: bool = ...,
        float_format: Optional[str] = ...,
        double_format: Optional[str] = ...,
        use_field_number: bool = ...,
        descriptor_pool: Optional[DescriptorPool] = ...,
        message_formatter: Optional[_MessageFormatter] = ...,
        print_unknown_fields: bool = ...,
        force_colon: bool = ...,
    ) -> None: ...
    def PrintMessage(self, message: Message) -> None: ...
    def PrintField(self, field: FieldDescriptor, value: Any) -> None: ...
    def PrintFieldValue(self, field: FieldDescriptor, value: Any) -> None: ...

def Parse(
    text: str,
    message: _M,
    allow_unknown_extension: bool = ...,
    allow_field_number: bool = ...,
    descriptor_pool: Optional[DescriptorPool] = ...,
    allow_unknown_field: bool = ...,
) -> _M: ...
def Merge(
    text: str,
    message: _M,
    allow_unknown_extension: bool = ...,
    allow_field_number: bool = ...,
    descriptor_pool: Optional[DescriptorPool] = ...,
    allow_unknown_field: bool = ...,
) -> _M: ...
def MergeLines(
    lines: Iterable[str],
    message: _M,
    allow_unknown_extension: bool = ...,
    allow_field_number: bool = ...,
    descriptor_pool: Optional[DescriptorPool] = ...,
    allow_unknown_field: bool = ...,
) -> _M: ...

class _Parser:
    allow_unknown_extension: bool = ...
    allow_field_number: bool = ...
    descriptor_pool: Optional[DescriptorPool] = ...
    allow_unknown_field: bool = ...
    def __init__(
        self,
        allow_unknown_extension: bool = ...,
        allow_field_number: bool = ...,
        descriptor_pool: Optional[DescriptorPool] = ...,
        allow_unknown_field: bool = ...,
    ) -> None: ...
    def ParseLines(self, lines: Iterable[str], message: _M) -> _M: ...
    def MergeLines(self, lines: Iterable[str], message: _M) -> _M: ...

class Tokenizer:
    token: str = ...
    def __init__(self, lines: Iterable[str], skip_comments: bool = ...) -> None: ...
    def LookingAt(self, token: str) -> bool: ...
    def AtEnd(self) -> bool: ...
    def TryConsume(self, token: str) -> bool: ...
    def Consume(self, token: str) -> None: ...
    def ConsumeComment(self) -> str: ...
    def ConsumeCommentOrTrailingComment(self) -> Tuple[bool, str]: ...
    def TryConsumeIdentifier(self) -> bool: ...
    def ConsumeIdentifier(self) -> str: ...
    def TryConsumeIdentifierOrNumber(self) -> bool: ...
    def ConsumeIdentifierOrNumber(self) -> str: ...
    def TryConsumeInteger(self) -> bool: ...
    def ConsumeInteger(self, is_long: bool = ...) -> int: ...
    def TryConsumeFloat(self) -> bool: ...
    def ConsumeFloat(self) -> float: ...
    def ConsumeBool(self) -> bool: ...
    def TryConsumeByteString(self) -> bool: ...
    def ConsumeString(self) -> Text: ...
    def ConsumeByteString(self) -> bytes: ...
    def ConsumeEnum(self, field: FieldDescriptor) -> int: ...
    def ParseErrorPreviousToken(self, message: Message) -> ParseError: ...
    def ParseError(self, message: Message) -> ParseError: ...
    def NextToken(self) -> None: ...

def ParseInteger(text: str, is_signed: bool = ..., is_long: bool = ...) -> int: ...
def ParseFloat(text: str) -> float: ...
def ParseBool(text: str) -> bool: ...
def ParseEnum(field: FieldDescriptor, value: str) -> int: ...
