#Oskaras Piskorowski
#6rd October 2025
#Check an armstrong number

n=0
count=0
while n==0:
    n=input('Enter a number: ')
    for i in n:
        n=int(n)
        i=int(i)
        count+=i**3
    break
if count==n:
        print('The number you entered is an armstrong number')
else:
        print('The number you entered is not an armstrong number')
    
