# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.


import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"human", "computer", line))