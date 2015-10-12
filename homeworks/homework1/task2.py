s = input().split()
l = len(s)
u = 0
for i in range(0, l):
    u += int(s[i])
    i += 1
print(u/l)

