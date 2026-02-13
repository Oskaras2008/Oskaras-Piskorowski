#Oskaras Piskorowski
#13/2/26
#Square number assignment
import random
list1 =[]
reverselist = []
totallist1 = 0
totalreverselist = 0
counter = 0

while totallist1!=totalreverselist or totallist1==0 or totalreverselist== 0:
    list1 =[]
    reverselist = []
    totallist1 = 0
    totalreverselist = 0
    count = 0
    numberone = random.randint(10,99)
    numbertwo = random.randint(10,99)
    numberthree = random.randint(10,99)
    
    while count<3:
        list1.append(numberone)
        list1.append(numbertwo)
        list1.append(numberthree)
        print(numberone)
        print(numbertwo)
        print(numberthree)
        for i in list1:
            reversenumber = str(i)[::-1]
            reversenumber = int(reversenumber)
            reverselist.append(reversenumber)
            a = i**2
            totallist1+=a
            b = reversenumber**2
            totalreverselist+=b
            count+=1
            
if totallist1 ==totalreverselist:
    print("the sum of squares of ", list1 ,"is equal to the sum of the squares of the numbers' digits reversed ",reverselist)
    print("The sum of each square is",totallist1)
            
    
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
