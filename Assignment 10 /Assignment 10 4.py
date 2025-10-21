#Oskaras Piskorowski
#21st of October 2025
#Exercise 3
#For this question you may need to use indexing, slicing and the replace() method.
#Create a string from a given string where all occurrences of its first char have been
#changed to '$', except the first char itself.

word= input('Enter a word: ')
count=1

for i in word:
    count+=1
    
substring = word[1:count]

letter = word[0:1]
stringone=substring.replace(letter,'$')

print(letter+stringone)
