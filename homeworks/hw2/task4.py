def euclid(n, m):
    if m >= n:
        a = n
        n = m
        m = a
    if n % m == 0:
        return m
    return euclid(m, n % m)

a, *args = (int(i) for i in input().split())


def rpfilter(a, *args):
    rp = str()
    for arg in args:
        if euclid(a, arg) == 1:
            rp += str(arg) + " "
    if len(rp) == 0:
        return None
    return rp

print (rpfilter(a, *args))
