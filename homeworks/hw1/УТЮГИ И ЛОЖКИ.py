#����� � �����*************************
s=str(input())
n=int(input())
if s=='����':
    if n%10==0:
        print (str(n)+' ������')
    if n%10==1:
        if n%100!=11:
            print (str(n)+' ����')
        else:
            print (str(n)+' ������')
    if 2<=n%10<=4:
        if n%100==12 or n%100==13 or n%100==14:
            print (str(n)+' ������')
        else:
            print (str(n)+' �����')
    if 5<=n%10<=9:
        print (str(n)+' ������')
if s=='�����':
    if n%10==0:
        print (str(n)+' �����')
    if n%10==1:
        if n%100!=11:
            print (str(n)+' �����')
        else:
            print (str(n)+' �����')
    if 2<=n%10<=4:
        if n%100==12 or n%100==13 or n%100==14:
            print (str(n)+' �����')
        else:
            print (str(n)+' �����')
    if 5<=n%10<=9:
        print (str(n)+' �����')