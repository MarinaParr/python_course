subject = str(input())
n = int(input())
if subject == 'утюг':
    subjects = ['утюг', 'утюга', 'утюгов']
if subject == 'ложка':
    subjects = ['ложка', 'ложки', 'ложек']
if subject == 'гармошка':
    subjects = ['гармошка', 'гармошки', 'гармошек']
if subject == 'чайник':
    subjects = ['чайник', 'чайника', 'чайников']


def plural(n, subjects):
    if n % 10 == 0 or (n % 10 == 1 and n % 100 == 11):
        return (str(n) + " " + subjects[2])
    if 2 <= n % 10 <= 4 and (n % 100 == 12 or n % 100 == 13 or n % 100 == 14):
        return (str(n) + " " + subjects[2])
    if 5 <= n % 10 <= 9:
        return (str(n) + " " + subjects[2])
    if n % 10 == 1 and n % 100 != 11:
        return (str(n) + " " + subjects[0])
    if 2 <= n % 10 <= 4 and not n % 100 == 12:
        return (str(n) + " " + subjects[1])
    if 2 <= n % 10 <= 4 and not n % 100 == 13 or n % 100 == 14:
        return (str(n) + " " + subjects[1])
print(plural(n, subjects))
