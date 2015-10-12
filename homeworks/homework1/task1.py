s = str(input())
n = int(input())
if s == 'утюг':
    if n % 10 == 0:
        print (str(n)+' утюгов')
    if n % 10 == 1:
        if n % 100 != 11:
            print (str(n)+' утюг')
        else:
            print (str(n)+' утюгов')
    if 2 <= n % 10 <= 4:
        if n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
            print (str(n)+' утюгов')
        else:
            print (str(n)+' утюга')
    if 5 <= n % 10 <= 9:
        print (str(n)+' утюгов')
if s == 'ложка':
    if n % 10 == 0:
        print (str(n)+' ложек')
    if n % 10 == 1:
        if n % 100 != 11:
            print (str(n)+' ложка')
        else:
            print (str(n)+' ложек')
    if 2 <= n % 10 <= 4:
        if n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
            print (str(n)+' ложек')
        else:
            print (str(n)+' ложки')
    if 5 <= n % 10 <= 9:
        print (str(n)+' ложек')
