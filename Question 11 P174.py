#Author Oskaras Piskorowski
#Date 2nd September 2025
#Programme to compute simple interest and compund interest #

invest = int(input('How much money have you invested? '))
rate = int(input('What percentage is your annual interest rate? '))

ratepercent = rate/100
ratepercent = int(ratepercent)

time = int(input('How much years have you invested in this'))

interest = invest * rate * time // 100
interest = int(interest)

print('In',time,'Years, your interest amoount earned is at $',interest)

