# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш \.

import re
import sys


for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\\", line):
        print(line)
