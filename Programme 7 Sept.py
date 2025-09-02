#Author Oskaras Piskorowski
#Date 1st September 2025
#Programme Ask the user for total amount of bill and amount of diners and say how much each diner needs to pay

bill = input('how much did the bill cost?')
bill = int(bill)
diners = input('Amount of diners: ')
diners = int(diners)

each = bill / diners
each = int(each)

print('each diner pays $',each)