# попытка эффективно по памяти прочитать
f = open("yazkora.txt", "r")
for line in f:
    adjectives = str()
    words = line.split(" ")
    for word in words:
        print(word)
        if word[len(word)-1] == "o" and word[len(word)-2] == "y":
            adjectives += word
    print(adjectives)


# хоть как-нибудь считать
with open("yazkora.txt", "r") as f:
    text = f.read()
propositions = text.split(".")
for proposition in propositions:
    adjectives = str()
    words = proposition.split(" ")
    for word in words:
        if word[len(word)-1] == "o" and word[len(word)-2] == "y":
            adjectives += word
    print(adjectives)
