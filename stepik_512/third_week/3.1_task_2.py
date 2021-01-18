# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.
#
# Пример:
# s = "abababa"
# t = "aba"
#
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa
#
# Итого: 3

s, t = (input() for _ in range(2))
pos = -1
count = 0
while True:
    try:
        pos = s.index(t, pos+1)
        count += 1
    except ValueError:
        break

print(count)