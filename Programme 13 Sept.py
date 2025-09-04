#Author Oskaras Piskorowski
#Date 4th September
#Programme for user to enter a colour. If the colour is red, then print I like red too else print I dont like the colour, I like red

colour = input('Enter a colour: ')

if colour== 'red' or colour== 'RED' or colour == 'Red':
    print('I like red too')
else:
    print('I dont like',colour,'. I like red')