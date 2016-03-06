import sys
input = sys.stdin.read()
data = input.split('\n')
n = int(data[0])
q = int(data[n+1])
ancestors = dict()


def is_ancestor(name_1, name_2):
    if name_1 == name_2:
        return "Yes"
    elif ancestors[name_1] == None:
        return "No"
    elif name_2 in ancestors[name_1]:
        return "Yes"
    else:
        for ancestor in ancestors[name_1]:
            answer = is_ancestor(ancestor, name_2)
            if answer == 'Yes':
                return answer
        return answer

for i in range(1, n + 1):
    inf_about_class = data[i].split(" ")
    ancestors[inf_about_class[0]] = list()
    if len(inf_about_class) > 1:
        for i in range(2, len(inf_about_class)):
            ancestors[inf_about_class[0]].append(inf_about_class[i])
    else:
        ancestors[inf_about_class[0]] = None

for i in range(n + 2, n + q + 2):
    query = data[i].split(" ")
    name_1 = query[1]
    name_2 = query[0]
    print(is_ancestor(name_1, name_2))
