


























































'''
1.-
2.
print('x y z w f')
for x in 0,1:
   for y in 0,1:
      for z in 0,1:
         for w in 0,1:
            f = (w<=z) == (x <= (not(y))) and (x or z)
            if f == 0:
                print(x,y,z,w,int(f))
---

3.-
4.-
5/7. I = 28*2**13  k = 32*1024 N = 2**i i = I/k
     или
     original = 1024*768*23
     compress = 800*600*22
     economy = original - compress
     100*economy / 2**13
---

6/8.
K=0
for а1 in sorted('ЩРЮИ'):
   for а2 in sorted('ЩРЮИ'):
      for а3 in sorted('ЩРЮИ'):
         for а4 in sorted('ЩРЮИ'):
            for а5 in sorted('ЩРЮИ'):
               s = а1+а2+а3+а4+а5
               K+=1
               if  а1 == ('Щ') and а5 == ('И'): 
                  print(s,K)
---

7/9.
наименьший(A1:D1;1) если(и(L1;j1);1;0) счётесли

8/10.-
9/11.
k = 7  kodorovka = 12 = 4 (2**4 = 16>12)
7 * 4 = 28bit = 4 bait (округление в большую)
1 пользователь = 4 + 15(доп свед) = 19bait
на 150 польз. = 19*150 = 2850

10/12.
s = 'AB' * 52  # Исходная строка из 52 комбинаций "AB"

while 'AA' in s or 'BB' in s or 'AB' in s:
    if 'AA' in s:
        s = s.replace('AA', 'B', 1)  # Заменяем первое вхождение AA на B
    elif 'BB' in s:
        s = s.replace('BB', 'A', 1)  # Заменяем первое вхождение BB на A
    elif 'AB' in s:
        s = s.replace('AB', 'BA', 1)  # Заменяем первое вхождение AB на BA

print(s)

---

11/13.
    148.195.140.28
    ------------- x
    148.195.140.0

print(bin(140)[2:]) #перевести в 2ичную
100011|00 00011100 # №пк, после едениц в маске переводим в 10ич - 00 00011100
100011|00 00000000 # 10 нулей, 2**10 = 1024-2 = 1022 всего

---
12/14.

a = 8**1014 - 2**530 - 12
b = bin(a)[2:]
c = b.count('1')
print(c)

---
13/16.
from functools import lru_cache

@lru_cache()
def f(n):
    if n >= 2010:
        return n
    if n < 2010:
        return f(n + 3) + f(n + 2) + f(n + 1)

a = (f(2000) - 2 * (f(2002) + f(2003))) / f(2004)
print(a)

---

14/18.
    1   1+x ...  ...

    1+y  макс ...

---

15/23.

def f(a, b):
    if a > b or a == 16:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a + 2, b) + f(a * 3, b)

print(f(2, 9) * f(9, 18))


-----


69.ответы на всё
вместо цифр в "check = link(25096921)" пишешь свой ноиер кима

import requests
import json

def link(var):
    check = requests.get(f'https://kompege.ru/api/v1/variant/kim/{var}')
    return check

check = link(25096921)
data = check.json()
k = 1
if 'tasks' in data:
    tasks = data['tasks']
    for task in tasks:
        taskId = task.get('taskId')
        key = task.get('key')
        video = task.get('video')
        timecode = task.get('timecode')
        if not video:
            if key is not None:
                print(f"№{k} ({taskId}):", key)
        else:
            if key is not None:
                print(f"№{k} ({taskId}):", key)
        k += 1
else:
    print("В ответе нет информации о заданиях")

-----

70. этого небудет(вроде)

for x in '0123456789abcdefghijk':
   for y in '0123456789abcdefghijk':
       a=int(f'943697{x}21',21) - int(f'2{y}9253',21)
       if a%20==0:
          print(x,y,a/20)


k=0
for x in range(1,2031):
   if int(3**100-x)%3==0:
      k+=1
   if k==5:
      print(x)
'''
