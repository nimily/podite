from pod import (
    FixedLenArray,
    FixedLenBytes,
    FixedLenStr,
    Vec,
    Str,
    Bytes,
    U16,
    U32,
    pod,
    Bool,
    U8,
)


@pod
class Simple:
    num: U32
    string: Str


@pod
class MyStruct:
    a_builtin: U8
    # a_array: FixedLenArray[U8]
    a_string: Str
    # a_bytes: Bytes


def test_round_trip_bytes():
    val = MyStruct(8, "hi")
    print(val)
    serialized = MyStruct.to_bytes(val)
    deserialized = MyStruct.from_bytes(serialized)

    assert val == deserialized
