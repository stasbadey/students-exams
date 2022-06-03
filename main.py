import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from controller.student_controller import StudentController
from model.Model import Model
from view.View import View

class StudentsExamsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.view = View()
        self.model = Model()
        self.controller = StudentController()

        self.view.controller = self.controller
        self.model.view = self.view
        self.controller.model = self.model

    def build(self):
        return self.view


if __name__ == "__main__":
    StudentsExamsApp().run()
