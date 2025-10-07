#Oskaras Piskorowski
#6rd October 2025
#Write a program to enter numbers until the user enters 0. Then it should print the
#count of the positive and negative numbers entered. You can assume all input is
#numeric.

n=67
negative=0
positive=0
while n==67:
    a=int(input('Enter a number: '))
    if a>0:
        positive+=1
        continue
    elif a<0:
        negative+=1
        continue
    else:
        break

print('The amount of positive numbers you have entered is,',positive)
print('The amount of negative numbers you have entered is,',negative)
    
    