from abc import ABC, abstractmethod
from functools import wraps


class Client(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @abstractmethod
    async def open_session(*args, **kwargs) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def close_session(*args, **kwargs) -> None:
        raise NotImplementedError()
