#Oskaras Piskorowski
#24th of October 2025
#Q5. Write a program which asks the user to enter a string of digits, and a step size.
#Go through the string and add the first number plus all the numbers at the step size.

string=input('Enter a string of digits: ')
stepsize=int(input('Enter a step size: '))
total=0
b=string[0::stepsize]
for i in b:
    b=int(b)
    i=int(i)
    total+=i
print(total)