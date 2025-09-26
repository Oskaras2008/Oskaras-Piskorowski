# Author Oskaras Piskorowski
# Date 5th September 2025
# Programme to ask user to enter one, two or three, if they say one, say Thank you, for two say well done and three
#say correct anything else is an error

n = int(input('Enter a number: '))

if n == 1:
    print('Thank you')
if n == 2:
    print('Well done')
if n == 3:
    print('Correct')
if n >=4:
    print('Error message')
