import re
import sys

code_py = sys.stdin.read()
code_py = code_py.split('\n')
str_number = 0
for string in code_py:
    str_number += 1
    finding = re.findall('([\w]+) = ', string)
    if len(finding) != 0:
        print(str_number, finding[0])
