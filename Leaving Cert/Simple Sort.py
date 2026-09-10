#Oskaras Piskorowski

list = eval(input('Enter a list of numbers: '))
emptlist = []
c = len(list)
x = list[0]

while len(emptlist) != c:
    x = list[0]
    
    for i in list:
        
        if i<x:
            x = i
            continue
        
        else:
            pass
        
    list.remove(x)
    emptlist.append(x)
    continue
        
print(emptlist)
        