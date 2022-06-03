import os

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.fullscreen = 'auto'


class View:
    def __init__(self):
        self.controller = None

    class MainScreen(Screen):
        pass


    class ChoiceScreen(Screen):
        pass


    class ByAverageMarkScreen(Screen):
        def __init__(self, **kw):
            super().__init__(**kw)
            self.controller = None

        def search_student(self):
            if len(self.input.text) == 0:
                self.label_check.text = '''you didn't enter anything, please try again'''
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                if int(self.input.text) < 0 or int(self.input.text) > 10:
                    self.label_check.text = 'Invalid number entered, please try again'
                    self.clear()
                else:
                    self.label_check.text = ''
                    self.label_av.text = self.controller.find_student_by_average_mark(int(self.input.text))

        def delete_student(self):
            if len(self.input.text) == 0:
                self.label_check.text = '''you didn't enter anything, please try again'''
                self.clear()
            if self.input.text.isdigit() is False:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                if int(self.input.text) < 0 or int(self.input.text) > 10:
                    self.label_check.text = 'Invalid number entered, please try again'
                    self.clear()
                else:
                    self.label_check.text = ''
                    self.label_av.text = self.controller.delete_student_by_average_mark(int(self.input.text))

        def clear(self):
            self.label_av.text = ""
            self.input.text = ""
            self.label_check.text = ""

        def information_output(self, info):
            self.label_check.text = info


    class ByNumberOfGroupScreen(Screen):
        def __init__(self, **kw):
            super().__init__(**kw)
            self.controller = None

        def search_student(self):
            if len(self.input.text) == 0:
                self.label_check.text = '''you didn't enter anything, please try again'''
                self.clear()
            if self.input.text.isdigit() is False:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                if len(self.input.text) != 6:
                    self.label_check.text = 'Invalid data entered, please try again'
                    self.clear()
                else:
                    self.label_check.text = ''
                    self.label_av.text = self.controller.find_student_by_group(self.input.text)

        def delete_student(self):
            if len(self.input.text) == 0:
                self.label_check.text = '''you didn't enter anything, please try again'''
                self.clear()
            if self.input.text.isdigit() is False:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            else:
                if len(self.input.text) != 6:
                    self.label_check.text = 'Invalid data entered, please try again'
                    self.clear()
                else:
                    self.label_check.text = ''
                    self.label_av.text = self.controller.delete_student_by_group(self.input.text)

        def clear(self):
            self.label_av.text = ""
            self.input.text = ""
            self.label_check.text = ""

        def information_output(self, info):
            self.label_check.text = info


    class ByMarkAndSubjectScreen(Screen):
        def __init__(self, **kw):
            super().__init__(**kw)
            self.controller = None

        def search_student(self):
            if len(self.input_mark.text) == 0 or len(self.input_subject.text) == 0:
                self.label_check.text = '''you didn't enter anything, please try again'''
                self.clear()
            if self.input_mark.text.isdigit() is False:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            if self.input_subject.text.isdigit() is True:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()

            if len(self.input_mark.text) != 0 or len(self.input_subject.text) != 0 \
                    or self.input_mark.text.isdigit() is True or self.input_subject.text.isdigit() is True:
                if int(self.input_mark.text) < 0 or int(self.input_mark.text) > 10:
                    self.label_check.text = 'Invalid number entered, please try again'
                    self.clear()
                else:
                    self.label_check.text = ''
                    self.label_av.text = self.controller.find_student_by_mark_and_subject(int(self.input_mark.text),
                                                                                          self.input_subject.text)

        def delete_student(self):
            if len(self.input_mark.text) == 0 or len(self.input_subject.text) == 0:
                self.label_check.text = '''you didn't enter anything, please try again'''
                self.clear()
            if self.input_mark.text.isdigit() is False:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()
            if self.input_subject.text.isdigit() is True:
                self.label_check.text = 'Invalid number entered, please try again'
                self.clear()

            if len(self.input_mark.text) != 0 or len(self.input_subject.text) != 0 \
                    or self.input_mark.text.isdigit() is True or self.input_subject.text.isdigit() is True:
                if int(self.input_mark.text) < 0 or int(self.input_mark.text) > 10:
                    self.label_check.text = 'Invalid number entered, please try again'
                    self.clear()
                else:
                    self.label_av.text = self.controller.delete_student_by_mark_and_subject(
                        int(self.input_mark.text),
                        self.input_subject.text)

        def clear(self):
            self.label_av.text = ""
            self.input_mark.text = ""
            self.input_subject.text = ""
            self.label_check.text = ""

        def information_output(self, info):
            self.label_check.text = info

    class WindowManager(ScreenManager):
        pass


Builder.load_file(os.path.join(os.path.dirname(__file__), "UI.kv"))
