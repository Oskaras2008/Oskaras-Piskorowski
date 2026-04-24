# Please enter name:Oskaras Piskorowski
print("******************")
print("* Conversions *")
print("******************")
print("1) From teaspoons to ml")
print("2) From tablespoons to ml")
print("3) From cups to ml")
print("4) From ml to teaspoons")
print("5) From ml to tablespoons")
print("6) From ml to cups")
conversion = int(input("Please enter the conversion, Please select 1 to 6 for an option,Eg if you want to go from teaspoons to ml, please select 1:"))

if conversion == 1:
    teaspoons = float(input("Please enter number of teaspoons:"))
    ml = teaspoons * 5
    print("The ml is:", ml)
    
elif conversion == 2:
    tablespoons = float(input("Please enter number of tablespoons:"))
    ml = tablespoons * 15
    print("The ml is:", ml)
    
elif conversion == 3:
    cups = float(input("Please enter number of cups:"))
    ml = cups * 240
    print("The ml is:", ml)

elif conversion == 4:
    ml = float(input("Please enter number of ml:"))
    teaspoons = ml/5
    print("The number of teaspoons is:", teaspoons)


elif conversion == 5:
    ml = float(input("Please enter number of ml:"))
    tablespoons = ml / 15
    print("The number of tablespoons is:", tablespoons)


elif conversion == 6:
    ml = float(input("Please enter number of ml:"))
    cups = ml /240
    print("The number of cups is:", cups)


