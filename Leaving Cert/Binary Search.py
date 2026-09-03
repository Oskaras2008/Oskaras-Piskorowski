#Oskaras Piskorowski

list = eval(input('Enter a list of numbers: '))
list.sort()
element = int(input('Enter an element you want to look for: '))

low = 0
high = len(list)-1
middle = (low+high)//2
boolean = False

while element != middle:
    
    if element > list[middle]:
        low=middle+1
        middle = (low+high)//2
    
    elif element < list[middle]:
        high = middle -1
        middle = (low+high)//2
        
    if element == list[middle]:
        print(middle)
        boolean = True
        break
    
    else:
        print('-1')
        break
    
    