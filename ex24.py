print('давайте попрактикуемся!')
print('Вы должны знать об управляющих последовательностях с символом \\, которые:')
print('\n управляют переносом строк и \t отступами.')

poem = """
\tДля счастья
мне совсемнемного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда \n я быть с тобою рядом
\n\tи никогда не отпускать!
"""

print("----------------------------")
print(poem)
print('----------------------------')



five = 10 - 2 + 3 - 6
print(f'Здесь должна быть пятёрка: {five}')

def secret_formula():
    print('jelly_beans=five*500')

secret_formula()

def my_function(track):
  print(track + "id")

my_function("1st\n")
my_function("2nd\n")
my_function("3rd\n")

def my_function(fname, lname):
  print(fname + '___' + lname)

my_function("less", "pain")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Olga", "Tatiana", "Inna")

#ещё один способ форматирования строки
print('Начиная с: {}'.format(five))
#так же, как со строкой f""
print(f'У нас есть {beans} бобов, {jars} банок и {crates} ящиков.')

start_point = start_point/10
