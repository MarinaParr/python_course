import re
import sys

data = sys.stdin.read()
results = re.findall("(y|Y)ou", data)
counts = len(results)
print(counts)
