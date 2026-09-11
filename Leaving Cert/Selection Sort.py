#Oskaras Piskorowski

list = eval(input('Enter a list of numbers: '))
count = 0
c = len(list)
marker = 0
x = list[0]
b = 0


while count!= c:
    
    x = list[0]
    z =x
    
    for i in range(marker,c):
        
        
        if list[i] < x:
            x = list[i]
            b = i
        
    if i == len(list)-1 and x==z:
        marker+=1
        count+=1
        pass
    
    else:
        cc = list.index(z)
        list.pop(b)
        list.insert(cc,x)
        cc+=1
        list.insert(cc,z)
        
        marker+=1
        count+=1
    
print(list)
    
    
    
    
    
    
    