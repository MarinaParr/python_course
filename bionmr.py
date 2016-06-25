import re

n = 20 #int(input())

def making_table(file):
    with open("tab_"+file, "w") as t:
        with open(file, "r") as f:
            strings = f.readlines()
            int_names = strings[0].split(" ")
            int_names.remove(int_names[-1])
            numbers = [  map(float,s.strip().split(" ")) for s in strings[1:]]
            l = []
            for int_name in int_names:
                inf_about_int = re.split('~|::|--', int_name)
                inf_about_int[1] = str(int((inf_about_int[1]))//76)
                inf_about_int[4] = str(int((inf_about_int[4]))//76)
                name = '-'.join(inf_about_int)
                l.append(name)
            t.write('\t'.join(l)+"\n")
            length = len(numbers[0])
            k = 0
            for q in range((len(strings)//n)):
                j = 0
                while j != n:
                    l = [0 for x in range(length)]
                    for interactions in numbers[k:k+n]:
                        for i in range(length):
                            l[i] = l[i] + interactions[i]
                    j += 1
                    k += 1
                t.write("\t".join(str(x) for x in l)+"\n")


def reverse_table(file):
    with open(file, "r") as tab:
        with open("rev_"+file, "w") as rt:
            lis = [x.split() for x in tab]
            for x in zip(*lis):
                for y in x:
                    rt.write(y+'\t')
                rt.write('\n')

with open("list_of_files.txt", "r") as lf:
    files_names = lf.read().split("\n")
    for file_name in  filter(None, files_names):
        making_table(file_name)
        reverse_table("tab_"+file_name)
