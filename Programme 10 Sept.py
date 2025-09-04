#Author Oskaras Piskorowski
#Date 4th September
#Programme for user to input two numbers. Display the numbers with the least on first

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if (a>b):
    print(b,a)
elif (a<b):
    print(a,b)
else:
    print('Result uncertain')