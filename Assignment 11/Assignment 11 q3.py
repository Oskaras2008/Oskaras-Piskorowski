#Oskaras Piskorowski
#23rd of October 2025
#Q3. Write a program to take in a string which is a mixture of characters. Extract all the
#digits from the string and print their total.

string= input( 'Enter a string: ')
integer=0
t=0
for i in string:
    if i.isdigit()==True:
        i=int(i)
        integer+=i
    
print(integer)
