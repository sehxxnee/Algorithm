n1,n2=input().split()

n1=int(n1)
n2=int(n2)

amin=[]
amax=[]
bmin=[]
bmax=[]
num=0

while n1!=0:
    num=n1%10
    if num==5:
        amin.append(5)
        amax.append(6)

    elif num==6:
        amin.append(5)
        amax.append(6)

    else:
        amin.append(num)
        amax.append(num)
         
    n1=n1//10

 
while n2!=0:
    num=n2%10
    if num==5:
        bmin.append(5)
        bmax.append(6)

    elif num==6:
        bmin.append(5)
        bmax.append(6)

    else:
        bmin.append(num)
        bmax.append(num)
         
    n2=n2//10

amin.reverse()
amax.reverse()
bmin.reverse()
bmax.reverse()

aminnum=0
amaxnum=0

bminnum=0
bmaxnum=0
 
for x in amin:
    aminnum=aminnum*10+x

for x in amax:
    amaxnum=amaxnum*10+x

for x in bmin:
    bminnum=bminnum*10+x

for x in bmax:
    bmaxnum=bmaxnum*10+x

print(aminnum+bminnum, amaxnum+bmaxnum)
    
