people = 20
cats = 30
dogs = 15


if people < cats:
    print("Слишком много кошек! Мир обречен!")

if people < cats:
    print("Не так много кошек! Мир спасен!")

if people > dogs:
    print("Мир утоп в слюнях!")

if people > dogs:
    print("Мир сухой!")


dogs = 5

if people >= dogs:
    print("Людей больше или столько же, сколько собак.")

dogs = 30

if people <= dogs:
    print("Людей меньше или столько же, сколько собак.")

dogs = 20

if people == dogs:
    print("Людей столько же, сколько собак.")
