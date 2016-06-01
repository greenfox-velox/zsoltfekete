# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def line_of_the_file(file_name):
    try:
        f = open(file_name)
        file_lines = f.readlines()
        f.close()
        output = len(file_lines)
        print (output)

    except FileNotFoundError:
        print('File not exists')

line_of_the_file('test.txt')
line_of_the_file('tesdt.txt')
