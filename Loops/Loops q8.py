#Author Oskaras Piskorowski
#Date 9th September 2025
#Programme that prints the factorial of a non negative number

number = int(input('Write a number: '))
answer = 1 
for i in range(1, number+1):
    
    answer *= i
print(answer)
