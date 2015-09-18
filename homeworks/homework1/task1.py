#ÓÒÞÃÈ È ËÎÆÊÈ*************************
s=str(input())
n=int(input())
if s=='óòþã':
    if n%10==0:
        print (str(n)+' óòþãîâ')
    if n%10==1:
        if n%100!=11:
            print (str(n)+' óòþã')
        else:
            print (str(n)+' óòþãîâ')
    if 2<=n%10<=4:
        if n%100==12 or n%100==13 or n%100==14:
            print (str(n)+' óòþãîâ')
        else:
            print (str(n)+' óòþãà')
    if 5<=n%10<=9:
        print (str(n)+' óòþãîâ')
if s=='ëîæêà':
    if n%10==0:
        print (str(n)+' ëîæåê')
    if n%10==1:
        if n%100!=11:
            print (str(n)+' ëîæêà')
        else:
            print (str(n)+' ëîæåê')
    if 2<=n%10<=4:
        if n%100==12 or n%100==13 or n%100==14:
            print (str(n)+' ëîæåê')
        else:
            print (str(n)+' ëîæêè')
    if 5<=n%10<=9:
        print (str(n)+' ëîæåê')
