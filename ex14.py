from sys import argv

script, user_name, friend = argv
prompt = '> '

print(f'Привет, {user_name}, я - сценарий {script}.')
print(f'Я хочу тебе задать несколько вопросов.')
print(f"Я тебе нравлюсь, {user_name}?")
likes = input(prompt)

print(f'Где ты живёшь, {user_name}?')
lives = input(prompt)

print(f'На каком компьютере ты работаешь?')
computer = input(prompt)

print(f'Твоего друга зовут {friend}?')
drug = input(prompt)

print(f"""
Итак, ты ответил \"{likes}\" на вопрос, нравлюсь ли я тебе.
Ты живёшь {lives}. Не представляю где это.
И у тебя есть компьютер {computer}. Прекрасно!
Ты сказал, {drug}, на вопрос друг ли тебе {friend}. Хочу с ней познакомитсьcя)))
""")
