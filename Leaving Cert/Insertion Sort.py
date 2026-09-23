#Oskaras Piskorowski
#Insertion Sort

marker=1
num=0
list1 = eval(input("Enter a list of numbers: "))
c = 0
d = 1


for i in range(1,len(list1)):
    a = list1[num]
    b = list1[marker]
       
        if list1[num] > list1[marker]:
            list1.pop(marker)
            list1.pop(num)
            list1.insert(c,b)
            list1.insert(d,a)
        
            marker+=1
            num+=1
            c+=1
            d+=1
        
        
        else:
            marker+=1
            num+=1
            c+=1
            d+=1
            pass

    
print(list1)
           
      
