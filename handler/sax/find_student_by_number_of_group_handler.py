import xml.sax


class FindStudentByNumberOfGroupHandler(xml.sax.ContentHandler):
    def __init__(self, group_number: str):
        self._current_data = ""
        self._surname = ""
        self._name = ""
        self._succession = ""
        self._schedule = ""
        self._mark = ""
        self._group_number = group_number
        self._is_expected = False

    def startElement(self, tag, attributes):
        self._current_data = tag

        if tag == "group" and attributes["number"] == self._group_number:
            self._is_expected = True
            print("Group:", self._group_number)

    def endElement(self, tag):
        if self._is_expected is True:
            if self._current_data == "surname":
                print(f"Surname: {self._surname}")
            elif self._current_data == "name":
                print(f"Name: {self._name}")
            elif self._current_data == "succession":
                print(f"Succession: {self._succession}")

                self._is_expected = False
                self._current_data = ""

    def characters(self, content):
        if self._current_data == "surname":
            self._surname = content
        elif self._current_data == "name":
            self._name = content
        elif self._current_data == "succession":
            self._succession = content
