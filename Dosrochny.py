# 25
'''
def delit(n):
    d7 = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 10 == 7 and i != 7:
                d7.add(i)
            if n//i % 10 == 7 and n//i != 7:
                d7.add(n//i)
    return d7


count = 0
for n in range(700001, 10**10):
    rez = delit(n)
    if len(rez) > 0:
        print(n, min(rez))
        count += 1
        if count == 5:
            break
'''

'''
with open('c:\\123\\24_28765.txt') as f:
    s = f.readline()
pos = []
for i in range(len(s)-1):
    if s[i:i+2] == 'BC':
        pos.append(i)
maxlen = 0
for i in range(len(pos)-181):
    curlen = pos[i+181]-pos[i]
    maxlen = max(curlen,maxlen)
  
print(maxlen)
'''
# 27A
'''
from math import dist
def center(c):
    minr = 10**20
    for i in c:
        r = 0
        for j in c:
            r += dist(i, j)
        if r < minr:
            minr = r
            point = i
    return point


with open('c:\\123\\27_A_28766.txt') as f:
    k1, k2 ,redgigant= [], [],[]
    for i in f.readlines():
        i = i.replace(',', '.')
        x, y, type = i.split()
        x, y = float(x), float(y)
        if y > 10:
            k1.append((x, y))
        else:
            k2.append((x, y))
        if type[0]=='Y' and type[-3:]=='III':
            redgigant.append((x,y))
x1, y1 = center(k1)
x2, y2 = center(k2)
print(len(k1),len(k2),len(redgigant))
a1=10**10
a2=0
for p in redgigant:
    a1=min(a1,dist((x1,y1),p))
    a2=max(a2,dist((x1,y1),p))
print(a1*10000,a2*10000)
'''
# 27B

from math import dist
def center(c):
    countyellowgigant = 0
    minr = 10**20
    minryellow = 10**20
    for x1, y1, type1 in c:
        # rint(x1,y1,type1)
        # input()
        r = 0
        if type1[0] == 'Z' and len(type1) == 3 and type1[-1] == 'I':
            countyellowgigant += 1

        for x2, y2, type2 in c:
            r += dist((x1, y1), (x2, y2))
            if type1[0] == type2[0] == 'Z' and len(type1) == len(type2) == 3 and type1[-1] == type2[-1] == 'I':
                if not ((x1 == x2) and (y1 == y2)):
                    minryellow = min(minryellow, dist((x1, y1), (x2, y2)))

        if r < minr:
            minr = r
            point = x1, y1
    return point[0], point[1], minryellow, countyellowgigant


with open('c:\\123\\27_B_28766.txt') as f:
    k1, k2, k3 = [], [], []

    for i in f.readlines():
        i = i.replace(',', '.')
        x, y, typ = i.split()
        x, y = float(x), float(y)
        if x > 20:
            k1.append((x, y, typ))
        elif y > 23:
            k2.append((x, y, typ))
        else:
            k3.append((x, y, typ))

x2, y2, r2, c2 = center(k2)
x1, y1, r1, c1 = center(k1)
x3, y3, r3, c3 = center(k3)
b1 = min(r1, r2, r2)
print(b1*10000, dist((x1, y1), (x3, y3))*10000)
