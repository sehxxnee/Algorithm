def calculate(amount):
    coins=[500,100,50,10,5,1]
    returning=1000-amount
    count=0
    
    for coin in coins:
        count+=returning//coin  
        returning%=coin  
        
    return count

num=int(input())   

count=calculate(num)
print(count)