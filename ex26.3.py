from sys import argv

script, filename = argv

txt = open(filename, 'r')

print(f"Вот ваш файл {filename}:")
print(txt.read())

print("Снова укажите имя файла:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
