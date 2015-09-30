s = input()
l = len(s)
d = dict()
lst = list()
for i in range(0, l):
    lst.append(s[i])
lst.sort
i = 0
while i < l:
    if lst[i] not in d:
        d[lst[i]] = lst.count(lst[i])
    i += 1
l = list(d.keys())
l.sort()
for i in l:
    print(i, d[i])
