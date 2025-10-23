#Oskaras Piskorowski
#23rd of October 2025
#Q4. Write a program which asks the user to guess a number between 1 and 100
#inclusive. You can hardcode the number they are trying to guess. Prompt the user if they
#are too high or too low. They can have no more than 7 attempts. If they use more then 7
#print ‘Game Over’ and tell them the answer.

number=67
attempt=0

while attempt<7:
    n=int(input('Guess a number: '))
      
    if n>67:
        print('Too high')
    elif n<67:
        print('Too low')
    attempt+=1
    if attempt ==7:
        print('Ran out of tries')    
    if n==67:
        print('Correct')
        break
    