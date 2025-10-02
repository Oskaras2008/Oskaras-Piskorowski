#Oskaras Piskorowski
#2nd October 2025
#Program that Grades student

grade=1
count=0
total=0
while  grade>0:
    grade= int(input('Enter your grades: '))
    if grade <0:
        break
    total+= grade
    count+=1 
    
avg=total/count

if avg >=90:
    print('Your average grade is A')
elif avg >=80<=89:
    print('Your average grade is B')
elif avg >=70<=79:
    print('Your average grade is C')
elif avg >=60<=69:
    print('Your average grade is D')
else:
    print('Your average grade is F')

