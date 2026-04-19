#Oskaras Piskorowski
#23rd of October 2025
#Q1. Write a program to reverse a string using:
#• A for loop




word=input('Enter a word: ')
output = ''
x=-1
for i in word:
    output+=word[x]
    x-=1
    
print(output)
