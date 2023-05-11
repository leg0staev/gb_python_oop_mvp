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

        sp: Presenter = Presenter(v, sm)
        mp: Presenter = Presenter(v, mm)

        # sp.sumButtonClick()

        mp.multyplyButtonClick()


Main.main()