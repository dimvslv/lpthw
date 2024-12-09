from sys import argv

script, filename = argv

print(f'Содержимое файла {filename}:')

with open(filename) as txt:
    print(txt.read())
