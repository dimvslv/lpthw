from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C).")
print("Если вы хотите стереть файл, нажмите клавишу Enter.")

input('?')

print('открытие файла...')
target = open(filename, 'w')

print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю у вас 3 строки.")

line 1 = input('строка 1: ')
line 2 = input('строка 2: ')
line 3 = input("строка 3: ")

print('Это я запишу в файл.')

terget.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('И наконец, я закрою файл.')
target.close()
