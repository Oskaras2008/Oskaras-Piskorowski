#Oskaras Piskorowski
#23/1/26
#List assignment

#q9
list = eval(input('Enter a list: '))
a = []
length = len(list)
for i in range(0,length-1):
    a.insert(i+1,list[i])
a.insert(0,list[length-1])
print(a)