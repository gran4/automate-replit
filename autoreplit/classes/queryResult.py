from ..commonTyping import JsonType


class ResultError(Exception):
    pass


class QueryResultBase:

    __slots__ = ()
        
    def __init__(self, opname: str, json: JsonType) -> None:
        data = json["data"][opname]
        if data is None:
            raise ResultError("Result does not exist.")
        for key, value in data.items():
            self.__setattr__(key, value)

    def __str__(self) -> str:
        result = f"{self.__class__.__name__}("
        s: str
        for s in self.__slots__:

            result += f"{s}={getattr(self, s)}, "
        return result[:-2] + ")"

class QueryResult(QueryResultBase):
    pass