#Oskaras Piskorowski
#4th of November 2025
#Assignment 12 q 3
#formula

formula = input('enter a formula: ')

opening = '('
closing = ')'
if formula.count(opening)==formula.count(closing):
    print('same amount of opening and closing brackets')
    
else:
    print('not the same amount of opening and closing brackets')

