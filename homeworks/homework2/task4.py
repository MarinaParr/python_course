def euclid(n, m):
    if m >= n:
        m, n = n, m
    if n % m == 0:
        return m
    return euclid(m, n % m)

a, *args = (int(i) for i in input().split())


def rpfilter(a, *args):
    rp = list()
    for arg in args:
        if euclid(a, arg) == 1:
            rp.append(arg)
    if len(rp) == 0:
        return None
    return rp

if rpfilter(a, *args) == None:
    print(rpfilter(a, *args))
else:
    for i in rpfilter(a, *args):
        print (i, end=' ')
