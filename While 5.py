#Oskaras Piskorowski
#3rd October 2025
#Write a program that prints from 1 to n squared using a while loop, It shouldd stop the while loop when the iteration count reaches 50

n= int(input('Enter a number: '))
count=0

while n>0:
    count+=1
    print(count**2)
    if count == 50:
        break
    elif count>=n:
        break
    