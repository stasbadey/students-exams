from typing import List

from tabulate import tabulate

from model.entity.student import Student
import copy

class TableFabric:

    @staticmethod
    def student_table_creator(students: List[Student]):
        head = ["name", "surname", "succession"]
        studs: list = []
        s: list = []
        for i in students:
            s.append(i.get_name())
            s.append(i.get_surname())
            s.append(i.get_succession())
            a = copy.copy(s)
            studs.append(a)
            s.clear()

        return tabulate(studs, headers=head, tablefmt="grid", stralign="center")

    @staticmethod
    def bool_table_creator(bools: List[bool]):
        head = ["is deleted"]
        is_deleted: list = []
        s: list = []
        for i in bools:
            s.append(i)
            a = copy.copy(s)
            is_deleted.append(a)
            s.clear()

        return tabulate(is_deleted, headers=head, tablefmt="grid", stralign="center")



