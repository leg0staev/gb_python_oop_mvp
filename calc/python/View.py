class View:
    def getValue(self, title: str) -> int:
        return int(input(title))

    def display(self, data: int, title: str) -> None:
        print(f"{title} {data}")
