#Oskaras Piskorowski
#22/1/26
#List assignment

#q6
count=0
list = eval(input('Enter a list'))
num = int(input('Enter a number: '))
pos = 0
for i in list:
    if i==num:
        print('position',list.index(i)+1)
    count+=1
    if count == 0:
        print('Number not found')