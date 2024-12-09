from sys import argv

script, filename = argv

print('Введите имя файла:')
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
