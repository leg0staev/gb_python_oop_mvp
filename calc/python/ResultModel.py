from CalcModel import CalcModel
from Model import Model


class ResultModel(Model, CalcModel):

    def multiplyResult(self) -> int:
        return self.x * self.y

    def sumResult(self) -> int:
        return self.x + self.y

    def setX(self, value: int) -> None:
        self.x = value

    def setY(self, value: int) -> None:
        self.y = value
