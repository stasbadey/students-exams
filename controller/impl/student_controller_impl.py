import xml.sax
from typing import Any, List

from controller.student_controller import StudentController
from handler.dom.delete_by_average_mark_dom_handler import DeleteByAverageMarkDomHandler
from handler.sax.find_student_by_average_mark_handler import FindAverageMarkHandler, FindByAverageMarkHandler
from handler.sax.find_student_by_mark_and_subject_handler import FindStudentExamsHandler, \
    FindStudentByMarkAndSubjectHandler
from handler.sax.find_student_by_number_of_group_handler import FindStudentByNumberOfGroupHandler
from handler.sax.find_student_id_by_number_of_group_handler import FindStudentIdByNumberOfGroupHandler
from handler.util.table_fabric import TableFabric
from model.entity.student import Student


class StudentControllerImpl(StudentController):

    def __init__(self):
        pass

    def find_student_by_average_mark(self, average_mark: int) -> List[Student]:
        handler = FindAverageMarkHandler()

        self._open_sax_parser_connection(handler)

        self._count_avg_from_dict(handler.get_avgs(), average_mark)

        return TableFabric.student_table_creator(FindByAverageMarkHandler.students)

    def find_student_by_mark_and_subject(self, mark: int, subject: str) -> List[Student]:
        handler = FindStudentExamsHandler(mark, subject)

        self._open_sax_parser_connection(handler)

        self._parse_students_exams_from_dict(handler.get_students_exams())

        return TableFabric.student_table_creator(FindByAverageMarkHandler.students)

    def find_student_by_group(self, group_number: str) -> List[Student]:
        handler = FindStudentByNumberOfGroupHandler(group_number)

        self._open_sax_parser_connection(handler)

        return TableFabric.student_table_creator(FindStudentByNumberOfGroupHandler.students)

    def delete_student_by_average_mark(self, expected_avg_mark: int) -> List[bool]:
        handler = FindAverageMarkHandler()

        self._open_sax_parser_connection(handler)

        bools: List[bool] = []
        for student_id, avg_mark in handler.get_avgs().items():
            if next(iter(avg_mark)) == expected_avg_mark:
                dom_handler = DeleteByAverageMarkDomHandler(student_id)
                bools.append(dom_handler.delete_student_by_student_id())

        return TableFabric.bool_table_creator(bools)

    def delete_student_by_mark_and_subject(self, mark: int, subject: str) -> List[bool]:
        handler = FindStudentExamsHandler(mark, subject)

        self._open_sax_parser_connection(handler)

        bools: List[bool] = []
        for student_id, exam_number in handler.get_students_exams().items():
            dom_handler = DeleteByAverageMarkDomHandler(student_id)
            bools.append(dom_handler.delete_student_by_student_id())

        return TableFabric.bool_table_creator(bools)

    def delete_student_by_group(self, group_number: str) -> List[bool]:
        handler = FindStudentIdByNumberOfGroupHandler(group_number)

        self._open_sax_parser_connection(handler)

        bools: List[bool] = []
        for student_id in handler.get_student_id():
            dom_handler = DeleteByAverageMarkDomHandler(student_id)
            bools.append(dom_handler.delete_student_by_student_id())

        return TableFabric.bool_table_creator(bools)

    @staticmethod
    def _count_avg_from_dict(avgs: dict, expected_avg_mark: int):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        for student_id, avg_mark in avgs.items():
            if next(iter(avg_mark)) == expected_avg_mark:
                parser.setContentHandler(FindByAverageMarkHandler(student_id))

                parser.parse("students.xml")

    @staticmethod
    def _parse_students_exams_from_dict(students_exams: dict):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        for student_id, exam_number in students_exams.items():
            parser.setContentHandler(FindStudentByMarkAndSubjectHandler(student_id, next(iter(exam_number))[0]))

            parser.parse("students.xml")

    @staticmethod
    def _open_sax_parser_connection(handler: Any):
        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        parser.setContentHandler(handler)

        parser.parse("students.xml")
