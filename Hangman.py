#Oskaras Piskorowski
#1/30/2026
#Hangman game

word = 'arsenalnumberone'
result= ['_']*len(word)
lg = [ ]

turns=10

while turns>0:
    
    guess = str(input('guess a letter : '))
    
    if guess in lg:
        print('You guessed this letter')
        continue
    lg.append(guess)
    
    
        
    if guess in word:
        print('This letter was in the word')
        for j in range(len(word)):
        
            if word[j] == guess:
                result[j]=guess

    else:
        turns-=1
        print('This letter wasnt in the word')
        
    print(lg)
    print('Turns left: ',turns)
    print('Guess the word:',' '.join(result))
    print('------------------------------------------------')
    
    if turns ==0:
        print('You ran out of words')
        print('The word was:',word)
        
    if '_' not in result:
        print('you won!!')
        break 
    
    


        

