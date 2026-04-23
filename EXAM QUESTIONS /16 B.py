#Question16_B_OL
#Enter your name here:Oskaras Piskorowski
print('Welcome to my weekly steps tracker')
list = []

monday=int(input('Enter amount of steps done on Monday: '))
list.append(monday)
tuesday=int(input('Enter amount of steps done on tuesday: '))
list.append(tuesday)
wednesday=int(input('Enter amount of steps done on wednesday: '))
list.append(wednesday)
thursday=int(input('Enter amount of steps done on thursday: '))
list.append(thursday)
friday=int(input('Enter amount of steps done on friday: '))
list.append(friday)
saturday=int(input('Enter amount of steps done on saturday: '))
list.append(saturday)
sunday=int(input('Enter amount of steps done on sunday: '))
list.append(sunday)

print('This list for each day includes: ' ,list)

total = sum(list)
print('Total steps this week : ' ,total)
average = total / len(list)
average = round(average, 2)

print('Average: ',average)

largest = max(list)
smallest = min(list)

print('Largest steps:', largest)
print('Smallest steps:', smallest)
