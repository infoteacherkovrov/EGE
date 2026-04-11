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
