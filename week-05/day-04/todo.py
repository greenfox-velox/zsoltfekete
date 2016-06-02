import sys, os
import csv

class Todo():
    def __init__(self, file_name):
        self.file_name = file_name

    def show_the_usermanual(self):
        print('\n'+'Python Todo application'+'\n')
        print('============================'+'\n')
        print('Command line arguments:'+'\n')
        print('-l Lists all the tasks')
        print('-a Adds a new task')
        print('-r Removes an task')
        print('-c Completes an task'+ '\n')

    def menu(self):
        self.is_the_file_exist(self.file_name)
        if len(sys.argv) == 1 :
            self.show_the_usermanual()
        elif len(sys.argv) == 2 :
            self.check_the_second_attribute()
        elif len(sys.argv) == 3 :
            self.check_the_third_attribute()
        else:
            self.error_messages('to_much')

    def is_the_file_exist (self,self_name):
        try:
            f = open(self.file_name)
            f.close()
        except FileNotFoundError:
            self.error_messages('filenot')
            f = open(self.file_name,'w')
            f.close()

    def check_the_second_attribute(self):
        if sys.argv[1] == '-l':
            print(self.list_the_tasks())
        elif sys.argv[1] == '-a':
            self.error_messages('notask')
        elif sys.argv[1] == '-r':
            self.error_messages('noremove')
        else:
            self.error_messages('index')

    def check_the_third_attribute(self):
        if sys.argv[1] == '-a':
            self.add_task()
        elif sys.argv[1] == '-r' or sys.argv[1] == '-c':
            try:
                self.task_number = int(sys.argv[2])
                if sys.argv[1] == '-r':
                    self.remove_task()
                elif sys.argv[1] == '-c':
                    self.to_check()
            except ValueError:
                self.error_messages('index')
            except IndexError:
                self.error_messages('overindex')
        else:
            self.error_messages('unsuported')

    def list_the_tasks(self):
        f = open(self.file_name)
        list_file = list(csv.reader(f, delimiter=','))
        number = 1
        output = ''
        if list_file == []:
            f.close()
            return 'No todos for today!' + '\n'
        else:
            for element in list_file:
                output += str(number)+' - '+str(self.checked(element[0]))+' '+element[1]+'\n'
                number +=1
            f.close()
            return output

    def add_task(self):
        f = open(self.file_name, 'a')
        f.write(str(False)+','+sys.argv[2]+'\n')
        f.close()

    def remove_task(self):
        f = open(self.file_name,'r')
        list_file =f.readlines()
        list_file.remove(list_file[self.task_number-1])
        f.close()
        f = open(self.file_name,'w')
        for i in list_file:
            f.write(i)
        f.close()

    def to_check(self):
       f = open(self.file_name)
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

    def checked(self,element):
        if element == 'False':
            return('[ ]')
        else:
            return('[x]')

    def error_messages(self,msgtype):
        if msgtype == 'index':
            print('Unable to remove: Index is not a number!')
        elif msgtype == 'filenot':
            print('File does not exists!, But we make a new one for you!')
        elif msgtype == 'overindex':
            print('Unable to do: Index is out of bound!')
        elif msgtype == 'notask':
            print('Unable to add: No task is provided!')
        elif msgtype == 'noremove':
            print('Unable to remove:  No index is provided !')
        elif msgtype == 'nocheck':
            print('Unable to check:  No index is provided !')
        elif msgtype == 'unsuported':
            print('Unsupported argument')
        elif msgtype == 'checked':
            print('It is already checked!')
        elif msgtype == 'to_much':
            print('Please type only one command at the same time!')

todo = Todo('todo.csv')
todo.menu()
