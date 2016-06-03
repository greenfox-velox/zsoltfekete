from tkinter import *
import sys, os
import csv

root = Tk()

class Todo():
    def __init__(self,file_name):
        self.file_name = file_name

    def design(self):
        self.input_x = 30
        self.color ='#007F00'

        topframe =Frame(root,bg=self.color,width=25)
        frame =Frame(root, width=1000, height=1200 ,bg='white')
        todo_header = Label(root, text='ToDo_List',bg=self.color, fg='white',height=3,font=('Palatino', 64) )
        left_frame= Frame(root, width=250, height=1200 ,bg=self.color)
        left_frame.pack(fill=Y,side=LEFT)
        todo_header.pack(fill=X,)

        self.c = StringVar()
        todo_label = Label(root,textvariable=self.c, bg='white',fg=self.color,font=('Palatino', 32),justify=LEFT)
        todo_label.place(x=300, y=250,)

        check_the_list = Button(left_frame, text="Check the task",font=('Palatino', 18),command=self.label_0)
        check_the_list.place(x=60, y=250)

        add = Button(left_frame, text="Add",font=('Palatino',20), command=self.add_task)
        add.place(x=90, y=310,)
        self.add_text= Entry(root)
        self.add_text.place(x=self.input_x, y=350,)

        complete = Button(left_frame, text="Complete",font=('Palatino', 20),command=self.to_check)
        complete.place(x=70, y=400)
        self.complete_text= Entry(root)
        self.complete_text.place(x=self.input_x, y=440,)

        remove = Button(left_frame, text='Remove',font=('Palatino', 20),command=self.remove_task)
        remove.place(x=80, y=490)
        self.remove_text= Entry(root)
        self.remove_text.place(x=self.input_x, y=530,)
        frame.pack()

    def label_0(self):
        self.c.set(self.list_the_tasks())

    def list_the_tasks(self):
        f = open(self.file_name)
        list_file = list(csv.reader(f, delimiter=','))
        number = 1
        output = ''
        if list_file == []:
            f.close()
            return 'No todos for today!' + '\n'+'\n'+'\n'+'\n'+'\n' + 'Thank you for your attention!'
        else:
            for element in list_file:
                output += str(number)+' - '+str(self.checked(element[0]))+' '+element[1]+'\n'
                number +=1
            f.close()
            return output

    def add_task(self):
        if self.add_text.get() == "":
            self.c.set('Opps! Would you like to add a new task !')
        else:
            f = open(self.file_name, 'a')
            f.write(str(False)+','+self.add_text.get()+'\n')
            f.close()
            self.label_0()
            self.add_text.delete(0, END)

    def to_check(self):
        if self.complete_text.get() == "":
            self.c.set('Opps! Which task is done ?')
        else:
            f = open(self.file_name)
            self.task_number = int(self.complete_text.get())
            list_file = csv.reader(f, delimiter=',')
            output = []
            for i in list_file:
               output.append(i)
            if output[self.task_number-1][0] == 'True':
                self.error_messages('checked')
            else:
               output[self.task_number-1][0] = 'True'
            f.close()
            f = open(self.file_name, 'w')
            for i in output:
               f.write(i[0] + ',' + i[1] + '\n')
            f.close()
            self.label_0()
            self.complete_text.delete(0, END)

    def remove_task(self):
        if self.remove_text.get() == "":
            self.c.set('Opps! Give a task number, please !')
        else:
            self.task_number = int(self.remove_text.get())
            f = open(self.file_name,'r')
            list_file =f.readlines()
            list_file.remove(list_file[self.task_number-1])
            f.close()
            f = open(self.file_name,'w')
            for i in list_file:
                f.write(i)
            f.close()
            self.label_0()
            self.remove_text.delete(0, END)

    def checked(self,element):
        if element == 'False':
            return('[     ]')
        else:
            return('[ ✓ ]')

    def error_messages(self,msgtype):
        if msgtype == 'checked':
            print('It is already checked!')

todo=Todo('todo.csv')
todo.design()

if __name__ == '__main__':
	root.mainloop()
