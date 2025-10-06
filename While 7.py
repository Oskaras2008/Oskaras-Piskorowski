#Oskaras Piskorowski
#6rd October 2025
#Program that asks use to enter number between 10 and 20
#If number is higher than 20, print too high, if number is lower than 0, print too low

n=14

while 10<n<=20:
    n=int(input('Enter a number: '))
    if 10>n:
        print('Too low')

    elif n>20:
        print('Too high')


    elif 10<n<=20:
        print('Thank You')
