def combinations(n, k):
    if k > n:
        return 0
    if k == 0 or n == k:
        return 1
    return combinations(n - 1, k - 1) + combinations(n - 1, k)


with open("dict.txt", "r") as f:
    text = f.read()
    words = text.split('\n')
    adjectives = 0
    nouns = 0
    verbs = 0
    adj = 1
    i = 1
    for word in words:
        if word[-2:] == "yo":
            adjectives += 1
        if word[-2:] == "ka":
            nouns += 1
        if not (word[-2:] == "yo" or word[-2:] == "ka"):
            verbs += 1
    for i in range(1, adjectives+1):
        adj *= combinations(adjectives, i)**2
    answer = nouns*verbs*adj
    print(answer)
