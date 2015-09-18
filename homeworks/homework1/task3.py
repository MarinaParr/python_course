s=input().split()
l=len(s)
ch=list()
nech=list()
for i in range (0,l,2):
    ch.append(int(s[i]))
    ch.sort(reverse= False)
for i in range (1,l,2):
    nech.append(int(s[i]))
    nech.sort(reverse=True)
#print(ch,nech)
i=0
st=str()
while i<(l/2):
    st+=(str(ch[i])+' ')
    st+=(str(nech[i])+' ')
    i+=1
print(st)
