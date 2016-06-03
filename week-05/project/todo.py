import sys, os

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
            else:
                self.error_messages('unsuported')

    def list_the_tasks(self):
        try:
            f = open(self.file_name)
            list_file = f.readlines()
            f.close()
            number = 1
            output = ''
            if list_file == []:
                return 'No todos for today!' + '\n'
            else:
                for n in list_file:
                    output += (str(number)+ ' - ' + n)
                    number +=1
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
                f.write(sys.argv[2] + '\n')
                f.close()
        except FileNotFoundError:
            self.error_messages('filenot')
            self.create_missing_file()

    def remove_task(self):
        try:
            if len(sys.argv) == 2:
                self.error_messages('noremove')
            elif len(sys.argv) < int(sys.argv[2]):
                self.error_messages('index')
            else:
                task_number = int(sys.argv[2])
                f = open(self.file_name,'r')
                output = f.readlines()
                f.close()
                if len(output) >= task_number:
                    f = open(self.file_name,'w')
                    output.remove(output[task_number-1])
                    for i in output:
                        f.write(str(i))
        except ValueError:
            self.error_messages('index')
        except FileNotFoundError:
            self.error_messages('filenot')
            self.create_missing_file()

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
        elif type == 'notask':
            print('Unable to add: No task is provided!')
        elif type == 'noremove':
            print('Unable to remove:  No index is provided !')
        elif type == 'unsuported':
            print('Unsupported argument')

todo = Todo('hangya.txt')
todo.menu()
