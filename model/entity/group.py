class Group:
    def __init__(self, number: str):
        self._number = number

    def get_number(self) -> str:
        return self._number

    def set_number(self, number: str) -> None:
        self._number = number
