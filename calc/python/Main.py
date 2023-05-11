from Presenter import Presenter
from View import View
from ResultModel import ResultModel


class Main:
    # @staticmethod
    def main() -> None:
        mm: ResultModel = ResultModel()
        v: View = View()
        rp: Presenter = Presenter(v, mm)

        rp.multyplyButtonClick()
        rp.sumButtonClick()


Main.main()
