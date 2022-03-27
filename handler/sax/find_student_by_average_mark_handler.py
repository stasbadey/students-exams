import logging
import re
import xml.sax
from typing import List

from model.entity.student import Student


class FindAverageMarkHandler(xml.sax.ContentHandler):
    counter = 0
    prev_mark = 0

    def __init__(self):
        self._current_data = ""
        self._mark = ""
        self._id = ""
        self._avgs = {}

    def startElement(self, tag, attributes):
        self._current_data = tag
        if tag == "studentId":
            self._id = attributes['id']

    def endElement(self, tag):
        if self._current_data == "mark":
            if re.fullmatch(r'^\s*$', self._mark) is None:
                FindAverageMarkHandler.prev_mark = FindAverageMarkHandler.prev_mark + int(self._mark)
                FindAverageMarkHandler.counter += 1

                if FindAverageMarkHandler.counter % 3 == 0:
                    self._avgs[self._id] = {round(FindAverageMarkHandler.prev_mark / 3)}
                    FindAverageMarkHandler.prev_mark = 0

    def characters(self, content):
        if self._current_data == "mark":
            self._mark = content

    def get_avgs(self):
        return self._avgs


class FindByAverageMarkHandler(xml.sax.ContentHandler):
    students: List[Student] = []

    def __init__(self, student_id: str):
        self._current_data = ""
        self._student_id = student_id
        self.surname = ""
        self.name = ""
        self.succession = ""
        self.is_expected = False
        self._student = Student()

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "studentId" and attributes["id"] == self._student_id:
            self.is_expected = True
            self._student.set_id(self._student_id)

    def endElement(self, tag):
        if self.is_expected is True:
            if self._current_data == "surname":
                self._student.set_surname(self.surname)
            elif self._current_data == "name":
                self._student.set_name(self.name)
            elif self._current_data == "succession":
                self._student.set_succession(self.succession)

                if self._student.get_name() == "":
                    logging.warning("Name field of id {} is empty!".format(self._student_id))
                elif self._student.get_surname() == "":
                    logging.warning("Surname field of id {} is empty!".format(self._student_id))
                elif self._student.get_succession() == "":
                    logging.warning("Succession field is empty!")

                FindByAverageMarkHandler.students.append(self._student)
                self._current_data = ""
                self.is_expected = False

    def characters(self, content):
        if self._current_data == "surname":
            self.surname = content
        elif self._current_data == "name":
            self.name = content
        elif self._current_data == "succession":
            self.succession = content
