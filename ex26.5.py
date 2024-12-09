five = 10 - 2 + 3 - 6
print(f"Здесь должна быть пятерка: {five}")


def secret_formula(started):
    jelly_beans = int(started * 500)
    jars = int(jelly_beans / 1000)
    crates = int(jars / 100)
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# помните, что это еще один способ форматирования строки
print("Начиная с: {}".format(start_point))
# так же, как со строкой f""
print(f"У нас есть {beans} бобов, {jars} банок и {crates} ящиков.")

start_point = start_point / 10

print("Мы также можем сделать это таким образом:")
formula = secret_formula(start_point)
# простой способ применить список к форматируемой строке
print("У нас есть {} бобов, {} банок и {} ящиков.".format(*formula))
