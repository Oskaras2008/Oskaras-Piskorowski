#Oskaras Piskorowski
#22/1/26
#List assignment

#q4
count=1
list = eval(input('Enter a list with numbers between 1 and 12'))
for i in list:
    if i >10:
        list.remove(i)
        count+=1
        continue
    
for j in range(0,count):
    list.append(10)
    
for k in list:
    if k >10:
        list.remove(k)
print(list)
            