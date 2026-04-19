#Oskaras Piskorowski
#2nd October 2025
#Program that finds the mean of integers

n = 0
counter = 0
total = 0

while n != ' ':
        n = input('Enter a number: ')
        if n.isdigit():
            total += int(n)
            counter+=1
        else:
            break 
print(total/counter)
