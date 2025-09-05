# Author Oskaras Piskorowski
# Date 5th September 2025
# Programme to display the water bill charges for the month provided the user gives a water unit summary
#5 cents a unit for the first 100 units
#10 cents a unit for the next 150 units
#20 cents a unit for anything over 250 units

water = int(input('How much units of water did you use this month'))

if 100 < water <=250:
    print('Your monthly charge is',(100*5+(water-100)*10)/100,'euros')
elif water >250:
    print('Your monthly charge is',(100*5+150*10+(water-250)*20)/100,'euros')
else:
    print('Your monthly charge is',(water* 0.05),'euros')