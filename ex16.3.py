from sys import argv

script_name, file_name = argv

print(f'я собираюсь вывести файл проекции {file_name} на экран')

prj = open(file_name)

print('вот его содержимое:')

print(prj.read())

print("а теперь по-другому.\nВведи имя файла:")
file_again = input("> ")

prj_again = open(file_again)

print(prj_again.read())
