#Oskaras Piskorowski
#23/1/26
#List assignment

#q10
list =[0,1]
count1 = 0
count2 = 1
length = len(list)
for i in range(0,21):
    list.append(list[count1]+list[count2])
    count1+=1
    count2+=1
    if count1 == 20:
        break
print(list)