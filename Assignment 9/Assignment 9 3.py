#Oskaras Piskorowski
#17th of October 2025
#Assignment 9 q 3
#Q3. Ask the user to enter a word and print the word modified as follows:
#• If the first letter of the word is a vowel, add ‘way’ to the end. So, if the user enters
#‘apple’ it should output ‘appleway’.
#• If the first letter of the word is a consonant, move the first letter to the end and
#add ‘ay’. So, if the user enters ‘pear’, it should output ‘earpay’.

word = str(input('Enter a word: '))
count=0

for i in word:
    count+=1

if (word[0]== 'a') or (word[0]== 'e') or (word[0]== 'i') or (word[0]== 'o') or (word[0]== 'u') or (word[0]== 'A') or (word[0]== 'E') or (word[0]== 'I') or (word[0]== 'O') or (word[0]== 'U'):
    together= word+'way'
    print(together)
else:
    count=int(count)
    newword=word[1:count]
    newword=str(newword)
    togetherone=newword+word[0]+'ay'
    print(togetherone)
