#Oskaras Piskorowski
#22/1/26
#List assignment

#q8
list1 = eval(input('Enter a list: '))
list2 = eval(input('Enter a list: '))
list3 = []
for i in range(0,len(list1)):
    a=list1[i]+list2[i]
    list3.append(a)
print(list3)

