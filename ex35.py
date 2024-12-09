from sys import exit

def gold_room():
    print('Здесь полно золота. Сколько кг ты унесёшь?')

    choice = input('> ')
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('Эй, ввест надо число')

    if how_much < 50:
        print('Шикарно! Ты не жадный, поэтому выигрываешь!')
        exit(0)
    else:
        dead('Ах ты жадина!')

def bear_room():
    print('Здесь спит медведь.')
    print('У медведя бочка с мёдом.')
    print('Медведь закрыл собой дверь выхода.')
    print('Как переместить медведя? Отобрать мед или подразнить медведя?')
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == 'отобрать мед':
            dead('Медведь посмотрел на тебя и ударил лапой по лицу.')
        elif choice == 'подразнить медведя' and not bear_moved:
            print('Медвведь отошёл от двери.')

            print('Вы можете войти в неё. Подразнить медведя или войти в дверь?')
            bear_moved = True
        elif choice == 'подразнить медведя' and bear_moved:
            dead('Медведь разозлился и зарычал на тебя.')
        elif choice == 'войти в дверь' and bear_moved:
            gold_room()
        else:
            print('Введите одно из предложенных действий.')

def cthuihu_room():
    print('На тебя смотрит великий и ужасный Ктулху.')
    print('Он смотрит на тебя, и ты начинаешь сходить с ума.')
    print('Убежать или начать сражаться?')

    choice = input('> ')

    if 'убежать' in choice:
        start()
    elif 'начать сражаться' in choice:
        dead('Хм, возможно, даже удастся победить!')
    else:
        cthuihu_room()

def dead(why):
    print(why, 'Великолепно!')
    exit(0)

def start():
    print('Ты в тёмной комнате.')
    print("Отсюда ведут две двери, налево и направо.")
    print('Куда ты повернёшь?')

    choice = input('> ')

    if choice == 'налево':
        bear_room()
    elif choice == 'направо':
        cthuihu_room()
    else:
        dead('Ты ходишь из комнаты в комнату, пока не умираешь с голоду.')

start()
