from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(2)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open (input_file)

print('первым делом выведем этот файл целиком:\n')

print_all(current_file)

print('Теперь отмотаем назад словно это кассета.')


rewind(current_file)

print('выведем шесть строк:')

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
