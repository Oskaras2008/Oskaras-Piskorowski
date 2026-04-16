#Oskaras Piskorowski
#23/1/26
#List assignment

#q11
list=eval(input('Enter a list of strings: '))
count1 = 0
biggest = 0
for i in list:
    count1+=len(i)
    if count1 > biggest:
        biggest = count1
    count1 = 0
print(biggest)
