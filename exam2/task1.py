import requests
import re

with open("hp5.txt", "r") as f:
    text = f.read().replace("\n", " ")
    whispers_up_2 = re.findall('([A-Z]\w+ [A-Z]\w+ whispered)', text)
# Я понимаю, что таким способом мы Aunt Petunia и Petunia учитываем дважды,
# но лучше придумать не могу пока
    whispers_up_1 = re.findall('([A-Z]\w+ whispered)', text)
    whispers_down_1 = re.findall('(whispered [A-Z]\w+)', text)
    whispers_down_2 = re.findall('(whispered [A-Z]\w+ [A-Z]\w+)', text)
    l = list()
    for i in whispers_up_1:
        l.append(i)
    for i in whispers_up_2:
        l.append(i)
    for i in whispers_down_1:
        l.append(i)
    for i in whispers_down_2:
        l.append(i)
    d = dict()
    for i in l:
        if i not in d:
            d[i] = l.count(i)
    counts = list()
    for key in d:
        counts.append(d[key])
    for key in d:
        if d[key] == max(counts):
            print (d[key], key)
