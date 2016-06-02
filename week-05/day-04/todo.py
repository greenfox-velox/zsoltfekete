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
        
            if len(sys.argv) == 1 :
                self.show_the_usermanual()
            elif sys.argv[1] == '-l':
                print(self.list_the_tasks())
            elif sys.argv[1] == '-a':
                self.add_task()
            elif sys.argv[1] == '-r':
                self.remove_task()
            elif sys.argv[1] == '-c':
                self.to_check()
            else:
                self.error_messages('unsuported')

    def checked(self,element):
        if element == 'False':
            return('[ ]')
        elif element == 'True':
            return('[x]')

    def list_the_tasks(self):
        try:
            f = open(self.file_name,)
            list_file = csv.reader(f, delimiter=',')
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
        except FileNotFoundError:
            self.error_messages('filenot')
            self.create_missing_file()

    def add_task(self):
        try:
            if len(sys.argv) == 2 :
                self.error_messages('notask')
            else:
                f = open(self.file_name, 'a')
                f.write(str(False)+','+sys.argv[2]+'\n')
                f.close()
        except FileNotFoundError:
            self.error_messages('filenot')
            self.create_missing_file()

    def remove_task(self):
        if len(sys.argv) == 2:
            self.error_messages('noremove')
        else:
            task_number = int(sys.argv[2])
            f = open(self.file_name,'r')
            list_file =f.readlines()
            try:
                list_file.remove(list_file[task_number-1])
            except ValueError:
                self.error_messages('index')
            except IndexError:
                self.error_messages('overindex')
            except FileNotFoundError:
                self.error_messages('filenot')
                self.create_missing_file()
            f.close()
            f = open(self.file_name,'w')
            for i in list_file:
                f.write(i)
            f.close()

    def to_check(self):
        if len(sys.argv) == 2:
           self.error_messages('index')
        else:
           try:
               task_number = int(sys.argv[2])
               f = open(self.file_name)
               list_file = csv.reader(f, delimiter=',')
               output = []
               for i in list_file:
                   output.append(i)
               if output[task_number-1][0] == 'True':
                    self.error_messages('checked')
               else:
                   output[task_number-1][0] = 'True'
               f.close()

               f = open(self.file_name, 'w')
               for i in output:
                   f.write(i[0] + ',' + i[1] + '\n')
               f.close()
           except IndexError:
                self.error_messages('overindex')
           except ValueError:
               self.error_messages('nocheck')

    def create_missing_file(self):
        f = open(self.file_name,'a')
        if sys.argv[1] == '-a':
            f.write(sys.argv[2] + '\n')
        f.close()

    def error_messages(self,type):
        if type == 'index':
            print('Unable to remove: Index is not a number !')
        elif type == 'filenot':
            print('File does not exists!, But we make a new one for you!')
        elif type == 'overindex':
            print('Unable to do: Index is out of bound!')
        elif type == 'notask':
            print('Unable to add: No task is provided!')
        elif type == 'noremove':
            print('Unable to remove:  No index is provided !')
        elif type == 'nocheck':
            print('Unable to check:  No index is provided !')
        elif type == 'unsuported':
            print('Unsupported argument')
        elif type == 'checked':
            print('It is already checked')

todo = Todo('todo4446666.csv')
todo.menu()
