import inspect
from functools import lru_cache

FORMAT_AUTO = "FORMAT_AUTO"  # attempt to determine format
FORMAT_PASS = "FORMAT_PASS"  # rely on previously set AutoTagTypeValue
FORMAT_ZERO_COPY = "FORMAT_ZERO_COPY"  # use rust's in-memory format
FORMAT_BORSCH = "FORMAT_BORSCH"  # use borsch format

class _GetitemToCall:
    def __init__(self, name, func):
        self.name = name
        self.func = lru_cache()(func)

    def __getitem__(self, args):
        if isinstance(args, tuple):
            return self.func(self.name, *args)
        else:
            return self.func(self.name, args)

    def __str__(self):
        return f"{_GetitemToCall.__module__}.{self.name}"

    def __repr__(self):
        return str(self)


def resolve_name_mapping(mapping):
    if mapping is None:
        return lambda x: x
    elif mapping == "lower":
        mapping = str.lower
    elif mapping == "upper":
        mapping = str.upper
    elif mapping == "capitalize":
        mapping = str.capitalize
    return mapping


def get_calling_module(level=3):
    frame = inspect.stack()[level]
    return inspect.getmodule(frame[0])


def get_concrete_type(module, type_):
    if isinstance(type_, str):
        module_dict = {name: getattr(module, name) for name in dir(module)}
        return eval(type_, module_dict, dict())
    return type_
