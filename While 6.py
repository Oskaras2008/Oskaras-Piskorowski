#Oskaras Piskorowski
#3rd October 2025
#Program that enters numbers and when total is more than 50, stop

n=1
count=0

while n>0:
    n=int(input('Enter a number: '))
    count+=n
    if count>50:
          break 
