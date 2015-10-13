def prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    a = 3
    while a < x:
        if x % a == 0:
            return False
        a += 1
    return True
n = int(input())
for i in range(n):
    x = int(input())
    print (prime(x))
