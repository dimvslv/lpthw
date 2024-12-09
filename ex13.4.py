first = input('сколько тебе лет?')
second = input('сколько ты весишь?')

from sys import argv

script, first, second = argv
print('эта программа:', script)
print('твой возраст:', first)
print('твой вес:', second)
