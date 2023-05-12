from Model import Model
from View import View
from MultiplyModel import MultiplyModel
from SumModel import SumModel


class Presenter:

    view: View
    sumModel: SumModel
    multiplyModel: MultiplyModel

    def __init__(self, v: View, sm: SumModel, mm: MultiplyModel) -> None:
        self.view = v
        self.sumModel = sm
        self.multiplyModel = mm

    def sumButtonClick(self) -> None:
        a: int = self.view.getValue("a: ")
        b: int = self.view.getValue("b: ")

        self.sumModel.setX(a)
        self.sumModel.setY(b)

        result: int = self.sumModel.result()
        self.view.display(result, "sum: ")

    def multiplyButtonClick(self) -> None:
        a: int = self.view.getValue("a: ")
        b: int = self.view.getValue("b: ")
        self.multiplyModel.setX(a)
        self.multiplyModel.setY(b)
        result: int = self.multiplyModel.result()
        self.view.display(result, "multiply: ")