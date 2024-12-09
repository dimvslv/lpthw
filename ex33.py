i = 0
numbers = []

while i < 6:
    print(f"В начале знчение i равно {i}")
    numbers.append(i)

    i = i + 1
    print("текущие значения: ", numbers)
    print(f'В конце значение i равно {i}')

print("Значения: ")

for num in numbers:
    print(num)
