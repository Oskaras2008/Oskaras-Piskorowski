#Oskaras Piskorowski
#6rd October 2025
#Program that asks user to guess the value, if it is low, print too low, if it is too high, print too high

n=167
while n==167:
    guess=int(input('Guess my number: '))
    if guess>n:
        print('Too high')
    elif guess<n:
        print('Too low')
    else:
        print('Correct')
