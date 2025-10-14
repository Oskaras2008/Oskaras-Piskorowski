#Oskaras Piskorowski
#10th October 2025
#Assignment 8 20(a)

#numberator=n
#denominator=d
c=67
n=2
d=9
count=1
fraction=n/d

while c==67:
    count+=1

    
    print(fraction)
    
    if count==8:
        break
    if count%2==0:
        n+=3
        d+=4
        a=n
        b=d
        fraction = fraction -a/b
        
    if count%2==1:
        n+=3
        d+=4
        a=n
        b=d
        fraction = fraction +a/b
        
    if (count%2==1) or (count%2==0):
        continue
    
