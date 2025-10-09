#Oskaras Piskorowski
#9th October 2025
#Write a program to take an integer a as an input and check whether it ends with 4 or 8. If it ends with 4,
#print "ends with 4", if it ends with 8, print "ends with 8", otherwise print "ends with neither".

string=input('Enter a number: ')

if string[-1] == "4":
        print('Ends with 4')
elif string[-1]== "8":
        print('Ends with 8')
else:
        print('Ends with neither')   