#Oskaras Piskorowski
#7rd October 2025
#Write a program to convert Binary to Decimal

b=input('Enter a binary number: ')
count=0
final=0

for i in b:
    
    b=int(b)
    i=int(i)
    final+=i*2**count
    count+=1


print(final)

    