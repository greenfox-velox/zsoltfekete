from tkinter import *

class Statistic():
    def __init__(self,joey,boss,skeleton_1,skeleton_2,skeleton_3,canvas):
        self.joey = joey
        self.boss = boss
        self.skeleton_1 = skeleton_1
        self.skeleton_2 = skeleton_2
        self.skeleton_3 = skeleton_3
        self.canvas =canvas

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

    def draw_skeleton_stat_1(self):
        self.zero_x = 765
        self.zero_y = 440
        self.skeleton =PhotoImage(file = 'picture/skeleton.gif')
        self.color = 'blue'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.skeleton)
        self.canvas.create_text(self.zero_x+130,self.zero_y+70,text='Skeleton_1',fill=self.color,font=('Palatino',18),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.skeleton_1.level),fill=self.color,font=('Palatino',16),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.skeleton_1.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.skeleton_1.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.skeleton_1.curHP / self.skeleton_1.maxHP)*120, self.zero_y+215, fill=self.color, width=0)

    def draw_skeleton_stat_2(self):
        self.zero_x = 765
        self.zero_y = 440
        self.skeleton =PhotoImage(file = 'picture/skeleton.gif')
        self.color = 'blue'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.skeleton)
        self.canvas.create_text(self.zero_x+130,self.zero_y+70,text='Skeleton_2',fill=self.color,font=('Palatino',),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.skeleton_2.level),fill=self.color,font=('Palatino',16),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.skeleton_2.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.skeleton_2.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.skeleton_2.curHP / self.skeleton_2.maxHP)*120, self.zero_y+215, fill=self.color, width=0)

    def draw_skeleton_stat_3(self):
        self.zero_x = 765
        self.zero_y = 440
        self.skeleton =PhotoImage(file = 'picture/skeleton.gif')
        self.color = 'blue'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.skeleton)
        self.canvas.create_text(self.zero_x+130,self.zero_y+70,text='Skeleton_3',fill=self.color,font=('Palatino',22),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.skeleton_3.level),fill=self.color,font=('Palatino',16),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.skeleton_3.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.skeleton_3.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.skeleton_3.curHP / self.skeleton_3.maxHP)*120, self.zero_y+215, fill=self.color, width=0)

    def draw_boss_stat(self):
        self.zero_x = 765
        self.zero_y = 440
        self.boss_image =PhotoImage(file = 'picture/boss.gif')
        self.color = 'red'
        self.draw_rectangle(self.zero_x, self.zero_y, self.zero_x+200, self.zero_y+240, self.color, 3)
        self.draw_rectangle(self.zero_x+20, self.zero_y+30, self.zero_x+180, self.zero_y+125,self.color,2)
        self.canvas.create_image(self.zero_x+60,self.zero_y+75, image = self.boss_image)
        self.canvas.create_text(self.zero_x+140,self.zero_y+70,text='Boss',fill=self.color,font=('Palatino',22),justify='center')
        self.canvas.create_text(self.zero_x+140,self.zero_y+90,text='Level'+ '  ' + str(self.boss.level),fill=self.color,font=('Palatino',22),justify='center')
        self.canvas.create_text(self.zero_x+90,self.zero_y+150,text='Defend Point :'+'  '+str(self.boss.DP),fill=self.color,font=('Palatino',18),justify='left')
        self.canvas.create_text(self.zero_x+90,self.zero_y+175,text='Strike Point :'+'    '+str(self.boss.SP),fill=self.color,font=('Palatino',18),justify='left')
        self.draw_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+180, self.zero_y+215, self.color, 1)
        self.canvas.create_rectangle(self.zero_x+20, self.zero_y+195, self.zero_x+20+(self.boss.curHP / self.boss.maxHP)*120, self.zero_y+215, fill=self.color, width=0)
