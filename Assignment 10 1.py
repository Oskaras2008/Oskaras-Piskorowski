#Oskaras Piskorowski
#21st of October 2025

#Write some code to test all the Python string methods given on the Python reference
#guide. Make sure you understand how all of them work before moving on.

word_one = input('Enter a word')

print(word_one[2])
print(word_one[-2])
count =0
for i in word_one:
      count+=1
      
print(word_one[1:count-1])

print(word_one.upper())
print(word_one.lower())

wordcount = word_one.count('a')
print(wordcount)
wordfind = word_one.find('d')
print(wordfind)

print(word_one.replace('m','v'))
print(word_one.replace('d','r'))
print(word_one.islower())
print(word_one.isupper())
print(word_one.isalnum())
print(word_one.isalpha())
print(word_one.isdigit())
print(word_one.index('i'))
print(word_one.strip('drid'))
      


      
