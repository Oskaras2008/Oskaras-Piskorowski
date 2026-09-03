a=1
count = -1
list1 = []
while a !=0:
    a = int(input('Enter numbers into a list and enter 0 to stop'))
    list1.append(a)
b = int(input('Enter the number you intend to look for: '))
for i in list1:
    count+=1
    if list1[count] == b:
        print(b,'is in index',count)
    else:
        continue
 
 
 
 
#List1(count)