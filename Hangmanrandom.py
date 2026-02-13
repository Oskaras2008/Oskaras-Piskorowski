#Oskaras Piskorowski
#1/30/2026
#Hangman game
 
import random
 
words = [
    "cryptozoology",
    "phlegmatic",
    "xylophonist",
    "zephyrlike",
    "quizzical",
    "knapsack",
    "ventriloquism",
    "fjordbound",
    "psychopathology",
    "glyphs",
    "bizarrely",
    "juxtaposed",
    "whizzbang",
    "subcutaneous",
    "klystrons",
    "myrrh",
    "chthonic",
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "byzantium",
    "sphinxlike",
    "quetzalcoatl",
    "hypothyroidism",
    "schnapps",
    "lymphocyte",
    "phytoplankton",
    "rhythmless",
    "czarevitch",
    "xenomorph",
    "ziggurat",
    "blwyddyn",
    "pseudopseudohypoparathyroidism",
    "futzing",
    "djinn",
    "knighthood",
    "psychedelic",
    "whorfian",
    "fjelds",
    "quorum",
    "zyzzogeton",
    "thwack",
    "brrr",
    "jackdaws",
    "mnemonic",
    "floccinaucinihilipilification",
    "vortexes",
    "jeffrey",
    "arsenal"   
]
word = random.choice(words)
 
result= ['_']*len(word)
lg = [ ]
 
turns=7
 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
/|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
/|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
/|\  |
/    |
      |
=========''', '''
  +---+
  |   |
  O   |
/|\  |
/ \  |
      |
=========''']
 
 
while turns>0:
    guess = str(input('guess a letter : '))
    if guess in lg:
        print('You guessed this letter')
        print('------------------------------------------------')
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
    if turns == 7:
        pass
    elif turns == 6:
        print(HANGMANPICS[0])
    elif turns == 5:
        print(HANGMANPICS[1])
    elif turns == 4:
        print(HANGMANPICS[2])
    elif turns == 3:
        print(HANGMANPICS[3])
    elif turns == 2:
        print(HANGMANPICS[4])
    elif turns == 1:
        print(HANGMANPICS[5])
    elif turns == 0:
        print(HANGMANPICS[6])
    print(lg)
    print('Turns left: ',turns)
    print('Guess the word:',' '.join(result))
    print('------------------------------------------------')

 
    
    if turns ==0:
        print('You ran out of turns')
        print('The word was:',word)
    if '_' not in result:
        print('you won!!')
        break 