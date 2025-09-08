#Author Oskaras Piskorowski
#Date 8th September 2025
#Programme that sets a variable to 0. Ask user to enter 5 numbers, After each input ask if they want to add the number to the total.
#Add the number, else do not add the number, When they entered the 5 numbers, print the total


total = 0

for i in range (5):
    number = int(input('Enter a number'))
    adding= (input('do you want to add this to the total? '))
#for i in range (5):
    if adding == 'yes' or adding == 'Yes':
          total += number
    else: 
        pass
        
print(total)
                
        