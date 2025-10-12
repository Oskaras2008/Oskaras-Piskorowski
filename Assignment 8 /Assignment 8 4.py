#Oskaras Piskorowski
#10th October 2025
#Write a program to input N numbers and then print the second largest number.

maximum=0
secondmax=maximum
count=0
c=67
number=int(input('How many numbers will you enter'))
while c==67:
    n=int(input('Enter a number: '))
    if maximum<n:
        secondmax=maximum
        maximum=n
    elif secondmax<n and n !=maximum:
        secondmax=n
    count+=1
    if count==number:
        break
print(secondmax)
    


