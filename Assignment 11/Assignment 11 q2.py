#Oskaras Piskorowski
#23rd of October 2025
#Q2. Write a program to check if a string is a palindrome. A palindrome is a word or string
#that reads the same backwards and forwards. For example: racecar; rotator

word = input('enter a word ')

if word[::-1]==word:
    print('Palindrome')
else:
    print('Not a palindrome')
