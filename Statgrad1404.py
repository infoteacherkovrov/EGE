#25
'''
def isprime(n):
    for i in range(2,int(n**0.5)+1):
       if n%i==0:
           return False
    return True
def delit(n):
    s=set()
    k=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            if isprime(i):
                k.add(i)
            s.add(n//i)
            if isprime(n//i):
                k.add(n//i)
    return sum(s),len(k)

c=0
for n in range(4555706,10**10):
    if n%10!=3:
        s,k=delit(n)
        if n-s-k>0 and (n-s-k)%100==23:
            print(n)
            c+=1
            if c==5:
                break
'''
#24
'''
with open('c:\\123\\24.txt') as f:
    s=f.readline()

maxlen=0
l=0
r=0
while r<len(s):
    if s[r] in '13579':
        l=r
        r+=1
        countgl=0
        countsogl=0
        while r<len(s) and s[r].isalpha():
            if s[r] in 'AEIOUY':
                countgl+=1
            else:
                countsogl+=1
            r+=1
        
        if r<len(s) and s[r]==s[l] and countgl==countsogl:
            if maxlen<=r-l:
                maxlen=r-l
                pos=l
        r-=1
    r+=1
print(pos)
'''
#26
'''
with open('c:\\123\\26.txt') as f:
    n=int(f.readline())
    a=[]
    for i in f.readlines():
        size,t = map(int,i.split())
        a.append((size,t))
a.sort()
k=1
size,t=a[0]
for i in range(1,len(a)):
    size2,t2=a[i]
    if size+k+2000<size2 and t!=t2:
        size,t=size2,t2
        k+=1
print(k,size)
'''
