#Author Oskaras Piskorowski
#Date 1st September 2025
#Programme Ask user for 2 numbers then multiply the result of no1 and no2 by a 3rd number

number_one = input('Enter a number: ')
number_one = int(number_one )
number_two = input('Enter another number: ')
number_two = int(number_two )

total_one = number_one + number_two 
total_one = int(total_one)

number_three = input('Enter your last number: ')
number_three = int(number_three)

total_two= total_one * number_three
total_two = int(total_two)

print('The calculated result when you multiply your third number by the sum of your first and second number is:', total_two )