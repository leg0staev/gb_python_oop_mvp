from Model import Model
from View import View


class Presenter:

    view: View
    model: Model

    def __init__(self, v: View, m: Model) -> None:
        self.view = v
        self.model = m

    def sumButtonClick(self) -> None:
        a: int = self.view.getValue("a: ")
        b: int = self.view.getValue("b: ")

        self.model.setX(a)
        self.model.setY(b)

        result: int = self.model.sumResult()
        self.view.display(result, "sum: ")

    def multyplyButtonClick(self) -> None:
        a: int = self.view.getValue("a: ")
        b: int = self.view.getValue("b: ")
        self.model.setX(a)
        self.model.setY(b)
        result: int = self.model.multiplyResult()
        self.view.display(result, "multiply: ")