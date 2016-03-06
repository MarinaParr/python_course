l = list()
if issubclass(D, A):
    l.append("A")
if issubclass(D, B):
    l.append("B")
if issubclass(D, C):
    l.append("C")
l.sort()
s = str()
for i in range(0, len(l)):
    s += l[i] + ' '
print(s)
