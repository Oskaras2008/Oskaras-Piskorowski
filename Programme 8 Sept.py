#Author Oskaras Piskorowski
#Date 1st September 2025
#Programme Ask user to input random numbers of days and print out how many hours, minutes and seconds in the given amount of days

days = input('Put in a random amount of days')
days = int(days)

hours = days*24
hours = int(hours)

minutes = hours*60
minutes = int(minutes)

seconds = minutes*60
seconds = int(seconds)

print('There are' ,hours ,'hours in' ,days ,'Days')
print('There are' ,minutes ,'minutes in' ,days ,'Days')
print('There are' ,seconds ,'seconds in' ,days ,'Days')