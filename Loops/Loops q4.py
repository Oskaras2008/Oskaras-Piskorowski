#Author Oskaras Piskorowski
#Date 8th September 2025
#Programme that asks user to enter name and number print each letter on a different line for the same amount of numbers they asked for

name = input('Enter your name: ')
number = int(input('Enter a number: '))

for i in range(number):
    for letter in name:
        print(letter)
