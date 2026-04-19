#Oskaras Piskorowski
#9th October 2025
#Write a python program to do the following:
#1:Read integer X
#2:Determine the number of digits in X
#3:Form an integer Y that prints n, that is units of X, and n, the most significant figure of X
#4:Output Y

x=(input('Enter a number: '))
print(x)


total=0
for i in x:
    total=total+1
print(total)

total_one=0
for i in x:
    i=int(i)
    y=len(x)
    total_one+=1
    if total_one==1:
        break
print((y*10)+i)
