# Question 16(a)
# Name and School:Oskaras Piskorowski

import random

while True:
   
    s_name = input("Enter your surname: ")
    if s_name == "END":
        break

    f_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))
    eircode = input("Enter your Eircode: ")

    
    print(f"Hello {f_name} {s_name} you are {age} years old")

    if age >= 50:
        vaccine = "ADENO"
    else:
        vaccine = "MRNA"

    last_digit = int(eircode[-1])

    if last_digit % 2 == 0:
        centre = "Eastwood"
    else:
        centre = "Northfield"

    print(f"Your Eircode is {eircode}")
    print(f"You must attend {centre} for your vaccine")
    print(f"{f_name}, you will receive the {vaccine} vaccine")

  
    choice = input("Do you want to join the vaccine trial? (yes/no): ")

    if choice.lower() == "yes":
        vaccines = ["A", "B", "C"]
        trial_vaccine = random.choice(vaccines)
        print(f"You have been assigned vaccine {trial_vaccine}")

    end = input("If finished type 'END', otherwise press ENTER: ")
    if end == "END":
        break