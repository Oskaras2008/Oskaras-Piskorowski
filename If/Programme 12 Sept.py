#Author Oskaras Piskorowski
#Date 4th September
#Programme for user to enter a number between 10 and 20 inclusive. If they enter a number in this range print 'Thank you ' else print incorrect value entered

number = int(input('Enter a number between 10 and 20 inclusive: '))

             
if (number >= 10) and (number <=20):
    print('Thank you')
else:
    print('Incorrect value entered')
