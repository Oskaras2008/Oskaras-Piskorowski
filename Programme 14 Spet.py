#Author Oskaras Piskorowski
#Date 4th September
#Programme to ask for users age, if they are over 18, say you can vote if they are 17 say you can drive,
#if they are 16 say you can buy a lottery ticket. If they are 16 or younger, say you can go trick or treating

user_age = int(input('Enter your age '))

if (user_age  >= 18):
    print('You can vote ')
if (user_age == 17):
    print('You can drive')
if (user_age == 16):
    print('You can buy a lottery ticket')
if (user_age <=15):
    print('You can go trick or treating')