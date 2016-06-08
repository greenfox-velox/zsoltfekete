from tkinter import *
from character import *

class Statistic():
    def __init__(self,canvas,joey):
        self.canvas = canvas
        self.joey = joey

    def draw_rectangle(self,x,y,x2,y2,color,width):
        self.canvas.create_rectangle(x, y, x2, y2, outline=color , width= width)

    def draw_hero_stat(self):
        self.zero_x = 765
        self.zero_y = 40
        self.hero =PhotoImage(file = 'picture/herodown.gif')
        self.color = 'green'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.hero)
        self.canvas.create_text(self.zero_x+140,self.zero_y+70,text='Hero',fill=self.color,font=('Palatino',22),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.joey.level),fill=self.color,font=('Palatino',18),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.joey.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.joey.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.joey.curHP / self.joey.maxHP)*120, self.zero_y+215, fill=self.color, width=0)

    def draw_skeleton_stat(self):
        self.zero_x = 765
        self.zero_y = 440
        self.skeleton =PhotoImage(file = 'picture/skeleton.gif')
        self.color = 'blue'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.skeleton)
        self.canvas.create_text(self.zero_x+140,self.zero_y+70,text='Hero',fill=self.color,font=('Palatino',22),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.joey.level),fill=self.color,font=('Palatino',18),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.joey.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.joey.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.joey.curHP / self.joey.maxHP)*120, self.zero_y+215, fill=self.color, width=0)

    def draw_boss_stat(self):
        self.zero_x = 765
        self.zero_y = 440
        self.boss =PhotoImage(file = 'picture/boss.gif')
        self.color = 'red'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.boss)
        self.canvas.create_text(self.zero_x+140,self.zero_y+70,text='Hero',fill=self.color,font=('Palatino',22),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.joey.level),fill=self.color,font=('Palatino',18),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.joey.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.joey.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.joey.curHP / self.joey.maxHP)*120, self.zero_y+215, fill=self.color, width=0)
