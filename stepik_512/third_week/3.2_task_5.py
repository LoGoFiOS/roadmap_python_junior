# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"(\b\w+)\1\b", line):
        print(line)