# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический
# факт об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
#
# Пример входного файла:
# 31
# 999
# 1024
# 502
#
# Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring


import sys
import requests


def is_intersting(n):
    data = requests.get(f'http://numbersapi.com/{int(n)}/math?json')
    answer = data.json()
    return answer['found']


for n in sys.stdin:
    print("Interesting" if is_intersting(n) else "Boring")
