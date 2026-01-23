#Oskaras Piskorowski
#23/1/26
#List assignment

#q11 b
x=0
newlist =[]
list1 = eval(input('Enter a list: '))
number = int(input('Enter a number: '))
for i in range(0,len(list1)):
    newlist.insert(x,list1[i]+number)
    x+=1
print(newlist)