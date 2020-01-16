from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print('TextBox')


class DropDownList(UIControl):
    def draw(self):
        print('DropDownList')


def draw(controls):
    for control in controls:
        control.draw()
# Draw method is taking many different form and this determined
# at run time


ddl = DropDownList()
textbox = TextBox()
draw([textbox, ddl])
