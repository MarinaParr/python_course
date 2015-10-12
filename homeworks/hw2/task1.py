n, k = (int(i) for i in input().split())


def combinations(n, k):
    if k > n:
        return 0
    if k == 0 or n == k:
        return 1
    return combinations(n - 1, k - 1) + combinations(n - 1, k)
print (combinations(n, k))
