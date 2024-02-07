n,k=input().split()
n=int(n)
k=int(k)

list1=[]

for i in range(n):
    num=int(input())
    list1.append(num) 

list1.sort(reverse=True)

remaining=k
count=0

for coin in list1:
    count+=remaining//coin
    remaining%=coin

print(count)
    
    
