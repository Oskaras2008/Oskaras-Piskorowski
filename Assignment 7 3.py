#Oskaras Piskorowski
#7th October 2025
#Convert Decimal to Binary


string=''
d =input('Enter a decimal number')
binary = 0
c = 0

while c == 0:
    d = int(d)
    
    if d ==0:
        print(string)
        break
    
    if d%2 ==0:
        d=d//2
        binary=0
        string = str(binary)+string
        continue
    
    if d%2 ==1:
        d = d//2
        binary=1
        string = str(binary) +string
        continue
    else:
        break
  
    
        
    
    
