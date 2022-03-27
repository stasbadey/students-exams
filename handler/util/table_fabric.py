from typing import List

from tabulate import tabulate

from model.entity.student import Student


class TableFabric:

    @staticmethod
    def student_table_creator(students: List[Student]):
        head = ["name", "surname", "succession"]

        return students #tabulate(students, headers=head, tablefmt="grid", stralign="center")

    @staticmethod
    def bool_table_creator(bools: List[bool]):
        head = ["is deleted"]

        return tabulate(bools, headers=head, tablefmt="grid", stralign="center")



