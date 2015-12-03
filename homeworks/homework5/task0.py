import re
import sys

data = sys.stdin.read()
results = re.findall("you", data)
counts = results.count("you")
print(counts)
