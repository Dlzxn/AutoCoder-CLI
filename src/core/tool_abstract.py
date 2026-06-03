from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def _desc(self) -> dict:
        pass

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass