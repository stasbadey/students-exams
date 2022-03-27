class Student:
    def __init__(self, surname: str, name: str, succession: str):
        self._surname = surname
        self._name = name
        self._succession = succession

    def get_surname(self) -> str:
        return self._surname

    def set_surname(self, surname: str) -> None:
        self._surname = surname

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_succession(self) -> str:
        return self._succession

    def set_succession(self, succession: str) -> None:
        self._succession = succession
