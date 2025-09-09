#Author Oskaras Piskorowski
#Date 9th September 2025
#Programme that prints sum of all odd numbers of given number

number= int(input('Enter a number: '))
total = 0
for i in range(1,number+1):
    if i%2 ==1 :
        total = total+i
        print(total)
    else:
        pass 
    