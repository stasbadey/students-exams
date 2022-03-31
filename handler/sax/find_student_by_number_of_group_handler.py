import copy
import logging
import xml.sax
from typing import List

from model.entity.student import Student


class FindStudentByNumberOfGroupHandler(xml.sax.ContentHandler):
    students: List[Student] = []

    def __init__(self, group_number: str):
        self._current_data = ""
        self._surname = ""
        self._student_id = ""
        self._name = ""
        self._succession = ""
        self._schedule = ""
        self._mark = ""
        self._group_number = group_number
        self._is_expected = False
        self._student = Student()

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "group" and attributes["number"] == self._group_number:
            self._is_expected = True

        if tag == "studentId" and attributes["id"] == self._student_id:
            self._student.set_id(self._student_id)

    def endElement(self, tag):
        if self._is_expected is True:
            if self._current_data == "surname":
                self._student.set_surname(self._surname)
            elif self._current_data == "name":
                self._student.set_name(self._name)
            elif self._current_data == "succession":
                self._student.set_succession(self._succession)

                if self._student.get_name() == "":
                    logging.warning("Name field of id {} is empty!".format(self._student_id))
                elif self._student.get_surname() == "":
                    logging.warning("Surname field of id {} is empty!".format(self._student_id))
                elif self._student.get_succession() == "":
                    logging.warning("Succession field of id {} is empty!".format(self._student_id))

                student_copy = copy.copy(self._student)
                FindStudentByNumberOfGroupHandler.students.append(student_copy)
                self._is_expected = False
                self._current_data = ""

    def characters(self, content):
        if self._current_data == "surname":
            self._surname = content
        elif self._current_data == "name":
            self._name = content
        elif self._current_data == "succession":
            self._succession = content
