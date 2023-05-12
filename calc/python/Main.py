from Presenter import Presenter
from SumModel import SumModel
from View import View
from MultiplyModel import MultiplyModel


class Main:
    # @staticmethod
    def main() -> None:
        sm: SumModel = SumModel()
        mm: MultiplyModel = MultiplyModel()

        v: View = View()

        p: Presenter = Presenter(v, sm, mm)
        
        p.sumButtonClick()

        p.multiplyButtonClick()


Main.main()