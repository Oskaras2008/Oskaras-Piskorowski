#Oskaras Piskorowski
#12th of October 2025
#Program that prints every integer between 1 and n that is divisible by m, report if that number is odd or even

n=int(input('Enter a number: '))
m=int(input('Enter a number you want to divide by: '))
count=1

for i in range(n+1):
    count+=1
    if i%m==0 and count%2==0:
        print(i,'even')
    elif i%m==0 and count%2==1:
        print(i,'odd')
    else:
        continue
        
        
        

