#Question16_B_OL
#Enter your name here:Oskaras Piskorowski

#2 = direct
#5 = indirect
#122,125,132,135,155
c=5
list1 = []
list2 = []
print("Flight numbers are 122,125,132,135,155")
while c>0:

    number = str(input("Enter your flight number: "))

    if number[-1]== "2":
        list1.append(number)
    elif number[-1]== "5":
        list2.append(number)
    c-=1

    
print("direct=",list1)
print("indirect=" ,list2)
 
