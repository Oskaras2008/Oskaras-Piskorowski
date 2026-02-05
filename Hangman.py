#Oskaras Piskorowski
#1/30/2026
#Hangman game

word = 'oskaraspiskorowski'
result= ['_']*len(word)
lg = [' ']

turns=0

while turns<15:
    
    guess = str(input('guess a letter : '))
    print(lg)
    if guess in lg:
        print('You guessed this letter')
        continue
    lg.append(guess)
    turns+=1
    count = 0
    for j in word:
        
        if j == guess:
            result[count]=guess
            print('This letter was in the word')
        else:
            pass
        count+=1
    print(' '.join(result))
    
    
    

        