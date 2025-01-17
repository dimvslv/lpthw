# схема связей аббревиатур с названиями стран
states = {
    'Россия': 'RU',
    'Германия': 'DE',
    'Узбекистан': 'UZ',
    'Зимбабве': 'ZW',
    'Турция': 'TR'
}

# создание базового набора стран и некоторых городов в них
cities = {
    'UZ': 'Газли',
    'TR': 'Сарыгерме',
    'DE': 'Мюнхен'
}

# добавление нескольких городов
cities['ZW'] = 'Гверу'
cities['RU'] = 'Москва'

# вывод некоторых городов
print('-' * 10)
print("В стране ZW есть город: ", cities['ZW'])
print("В стране RU есть город: ", cities['RU'])

# вывод некоторых стран
print('-' * 10)
print("Аббревиатура Турции: ", states['Турция'])
print("Аббревиатура Германии: ", states['Германия'])

# выполняется с учетом страны и словаря городов
print('-' * 10)
print("В Турции есть город: ", cities[states['Турция']])
print("В Германии есть город: ", cities[states['Германия']])

# вывод аббревиатур всех стран
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} имеет аббревиатуру {abbrev}")

# вывод всех городов в странах
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"В стране {abbrev} есть город {city}")

# а теперь сразу оба типа данных
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"В стране {state} используется аббревиатура {abbrev}")
    print(f"и есть город {cities[abbrev]}")

print('-' * 10)
# безопасное получение аббревиатуры страны, которая не представлена
state = states.get('США')

if not state:
    print("Прошу прощения, США не существует или уничтожено.")

# получение города со значение по умолчанию
city = cities.get('US', 'не существует')
print(f"В стране 'US' есть город: {city}")

print(len(cities))
print(type(cities))

cities2 = dict(Almaty = 'KZ', Bishkek = 'KG')
print(cities)
print(cities2)
