#Question16_A_OL
#Enter your name here:Oskaras Piskorowski 

print("Welcome to the Step Tracker App!")
name = str(input("Enter your name: "))

steps_today = int(input("Enter the number of steps you walked today: "))
#This is where user inputs steps
if steps_today >=10000:
    print("Well done!", name ," You reached your goal.")
if steps_today <10000 and steps_today >5000:
    print("Almost there", name)
if steps_today <4999:
    print("Aim for more tomorrow", name)
if steps_today <0:
    print("Number cant be negative", name)