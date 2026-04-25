with open ('c:\\123\\24_28166.txt') as f:
    s=f.readline()
l=len(s)//6001
count_ww=0
for i in range(0,len(s),l):
    podp=s[i:i+l]
   
    ww=0
    for j in range(len(podp)-1):
        if podp[j]=='W' and podp[j+1]=='W':
            ww+=1

    pos=podp.find('WW')
    if ww>count_ww:
        count_ww=ww
        pos_ww=pos
        num=i//l+1
       
    elif ww==count_ww and pos>pos_ww:
        pos_ww=pos
        num=i//l+1
   
print(count_ww+num)
        
        
        
#25
'''
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
count=0
for n in range(10**6-1,100000-1,-1):
    for k in range(142917,10**6,142917):
        if isprime(n-k):
            print(n,abs(n-k-k))
            count+=1
            break
    if count==5:
        break
'''