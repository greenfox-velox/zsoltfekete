
from tkinter import *
from maps import *
from character import *


class Presentation(Character):
    def __init__(self,row,column):
        super().__init__(row,column)
        self.photo_presentation = PhotoImage(file = 'picture/presentation.gif')
        self.photo_slide_1 = PhotoImage(file = 'slide_1.gif')
        self.photo_slide_2 = PhotoImage(file = 'picture/presentation.gif')
        self.photo_slide_3 = PhotoImage(file = 'picture/presentation.gif')
        self.photo_slide_4 = PhotoImage(file = 'picture/presentation.gif')
        self.photo_slide_5  = PhotoImage(file = 'picture/presentation.gif')
        self.photo_slide_6  = PhotoImage(file = 'picture/presentation.gif')
        self.photo_slide_7  = PhotoImage(file = 'picture/presentation.gif')


    def draw_character(self, canvas):
        self.draw_image(self.photo_presentation, canvas)

    def presentation (self,canvas):
        canvas.create_image(400, 400, image = self.photo_slide_1)
