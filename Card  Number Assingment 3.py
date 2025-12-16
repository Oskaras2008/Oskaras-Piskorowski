#Oskaras Piskorowski
#15th December 2025
#November Assesment revision program 2

wincard = '8549018035096133'
last1 = wincard[-1]
last1 = int(last1)
excluding = wincard[-2::-1]

index=-1
string1=''
for i in excluding:
    string1+=excluding[index]
    index-=1
string2=''
for j in range(0,15,2):
    string2+=string1[j]
string3=''
for e in range(1,15,2):
    string3+=string1[e]
total=0
for i in string2:
    i=int(i)
    i=i*2
    if i>9:
        i=i-9
    total+=i
for j in string3:
    j=int(j)
    total+=j
last1=int(last1)
total+=last1
 
if total%10==0:
    print('valid')
else:
    print('invalid')