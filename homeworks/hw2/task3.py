def euclid(n, m):
    if m >= n:
        a = n
        n = m
        m = a
    if n % m == 0:
        return m
    return euclid(m, n % m)
n, m = (int(i) for i in input().split())
print(euclid(n, m))
