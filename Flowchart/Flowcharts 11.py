#Oskaras Piskorowski
#19th of September 2025
#Accept number till user enters zero are find their average

total=0
number = 1
count=0
while number != 0:
    number=float(input('Enter number: '))
    total += number
    count+=1
   
print(total/count)
