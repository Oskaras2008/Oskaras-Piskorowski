#Oskaras Piskorowski
#ExamCraft OL
#3.13.26

import random
words = ['cat','mat','can','man','pool','tool','mule','pat','tan','rule']
print('The list of words is', words)
random_words = words[random.randint(0,len(words) -1)]
guess = 0

print('The length of the word is: ',len(random_words))
print('The first letter of the word is:', random_words[0])
while guess<3:
    guess+=1
    guess1 = input('Guess the word')
    if guess1 == random_words:
        print('Well done')
        break
    elif guess1 != random_words:
        print('Incorrect')
        
print('The word was',random_words)
    