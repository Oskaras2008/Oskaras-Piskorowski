#For loops
# For loops are used to iterate over a sequence
#so for us, a string or range of numbers

#For loop through the numbers 1-5
for i in range(6):
    print(i, end=', ')
    
fruit = input('enter a fruit')
for letter in fruit:
    for i in range(3):
        print(letter)
