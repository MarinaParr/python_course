import re
import sys

code_py = sys.stdin.read()
code_py = code_py.split('\n')
str_number = 0
for string in code_py:
    str_number += 1
    finding = re.match(' *([\w,. ]+) = ', string)
    # print(finding)
    if finding is not None:
        match = list(finding.groups())
        for element in match:
            elem = element.split(', ')
            answer = ' '.join(elem)
            print(str_number, answer)
