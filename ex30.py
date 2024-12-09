people = 30
cars = 30
trucks = 15


if cars > people:
    print("Поедем на машине.")
elif cars < people:
    print("Не поедем на машине.")
elif cars == people:
    print("Без разницы.")
else:
    print("Мы не можем выбрать.")


if trucks < cars:
    print("слишком много атобусов.")
elif trucks > cars:
    print("может поехать на автобусе?")
else:
    print("Мы до сих пор не можем выбрать.")

if people > trucks:
    print("хорошо, поедем на автобусе.")
else:
    print("Прекрасно, давайте останемся дома.")
