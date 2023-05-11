from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def multiplyResult(self) -> int:
        pass

    @abstractmethod
    def sumResult(self) -> int:
        pass

    @abstractmethod
    def setX(self, value: int) -> None:
        pass

    @abstractmethod
    def setY(self, value: int) -> None:
        pass
