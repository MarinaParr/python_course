import re
n = 20 #int(input())
with open("hb_trace.dat", "r") as data:
    strings = data.readlines()
    length = (len(strings)-1)//n
    int_names = strings[0].split(" ")
    int_names.remove(int_names[-1])
    l = []
    for int_name in int_names:
        inf = re.split('~|::|--', int_name)
        num_mol_f = str((int(inf[1]))//76)
        num_res_f = str(int(inf[1])%76)
        num_mol_s = str((int(inf[4]))//76)
        num_res_s = str(int(inf[4])%76)
        name = inf[0]+num_res_f+"~"+num_mol_f+"::"+inf[2]+"--"+inf[3]+num_res_s+"~"+num_mol_s+"::"+inf[5]
        l.append(name)
    d = dict()
    for elem in l:
        d[elem] = []
    for string in strings[1:]:
        string = string.split(" ")
        i = 0
        for elem in string[:len(string)-1]:
            d[l[i]].append(int(elem))
            i += 1
    for key in d:
        st = []
        k = 0
        while k != (len(d[key])//n):
            st.append(str((sum(d[key][k*20:k*20+20]))))
            k += 1
        d[key] = st
    l_inn = []
    l_out = []
    for key in d:
        name_elements = re.split('~|::|--', key)
        name = name_elements[0]+"_"+name_elements[2]+"_"+name_elements[3]+"_"+name_elements[5]
        if name_elements[1] == name_elements[4]:
            if name not in l_inn:
                l_inn.append(name)
        else:
            if name not in l_out:
                l_out.append(name)
    for i in range(48):#Number_of_molecules
        with open (str(i)+"_inner.txt", "w") as f:
            for element in l_inn:
                items = element.split("_")
                inn_int = items[0]+"~"+str(i)+"::"+items[1]+"--"+items[2]+"~"+str(i)+"::"+items[3]
                if inn_int in d:
                    f.write(inn_int+"\t"+"\t".join(d[inn_int])+"\n")
                else:
                    f.write(inn_int+"\t"+"\t".join([str(0) for x in range(length)])+"\n")
    for i in range (48):#Number_of_molecules
        with open (str(i)+"_outer.txt", "w") as f:
            for elem in l_out:
                items = elem.split("_")
                out_int= items[0]+"~"+str(i)+"::"+items[1]+"--"+items[2]+"~"+"?"+"::"+items[3]
                iis = re.split('~|::|--',out_int)
                q = 0
                for key in d:
                    if len(re.findall(iis[0]+"\~"+iis[1]+"::"+iis[2]+"--"+iis[3]+"\~"+"\d+"+"::"+iis[5],key)) != 0:
                        f.write(out_int+"\t"+"\t".join(d[key])+"\n")
                        q = 1
                if q == 0:
                    f.write(out_int+"\t"+"\t".join([str(0) for x in range(length)])+"\n")
