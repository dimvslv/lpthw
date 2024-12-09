def add(a,b):
    print(f'СЛОЖЕНИЕ {a} + {b}')
    return a + b

def subtract(a,b):
    print(f'ВЫЧИТАНИЕ {a} - {b}')
    return a - b

def multiply(a,b):
    print(f'УМНОЖЕНИЕ {a} * {b}')
    return a * b

def divide(a,b):
    print(f'ДЕЛЕНИЕ {a} / {b}')
    return a / b

print(add)
print(subtract)
print(multiply)
print(divide)

print('Давайте выполним несколько вычислений с помощью функций!')
print('Введите параметры 1 и 2')
print('>')
age = add(float(input()),float(input()))
print('Введите параметры 1 и 2')
print('>')
height = subtract(float(input()),float(input()))
print('Введите параметры 1 и 2')
print('>')
weight = multiply(float(input()),float(input()))
print('Введите параметры 1 и 2')
print('>')
iq=divide(float(input()),float(input()))

print(f'Возраст: {age},\nРост: {height},\nВес: {weight},\nIQ: {iq}')

# Головоломка в качестве дополнительного задания

print('Это головоломка.')

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print('Получается: ', what, "Вы можете вычислить это вручную?")
