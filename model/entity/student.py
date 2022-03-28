class Student:
    def __init__(self):
        self._surname = ""
        self._name = ""
        self._succession = ""
        self._id = ""

    def get_id(self) -> str:
        return self._id

    def set_id(self, id: str) -> None:
        self._id = id

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
