# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.


import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall("cat", line)) > 1:
        print(line)
