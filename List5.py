#Oskaras Piskorowski
#22/1/26
#List assignment

#q5

list= eval(input('Enter a list of strings: '))
list2 = []
string = ''
for i in list:
    string +=i
    string = string[1::]
    list2.append(string)
    string = ''
print(list2)