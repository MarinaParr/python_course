import re
import sys

pattern = '([\W]+|_)'
text = sys.stdin.read()
result = re.sub(pattern, " ", text)
print(result)
