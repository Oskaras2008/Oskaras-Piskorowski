#Oskaras Piskorowski
#9th October 2025
#Program to find largest number in list of numbers entered through keyboard

number=int(input('How much numbers will you enter'))
c=67
count=0
ten=0
while c==67:
    
    n=int(input('enter a number'))
    if n>count:
        count+=n
        
    ten+=1
    if ten==number:
        break
print(count)
        
    
