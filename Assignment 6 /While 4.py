#Oskaras Piskorowski
#3rd October 2025
#Program that prints every number to n and skips multiples of 5


n = int(input('Enter a number: '))
count=0
while n>0:
    for i in range(0,n):
        count+=1
        
        if count%5!=0:
            print(count)
            continue
    else:
        break 
        
