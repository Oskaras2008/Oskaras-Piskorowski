#Oskaras Piskorowski
#15th December 2025
#November Assesment revision progam 3

wincard = '8549018035096133'
last1 = wincard[-1]
last1 = int(last1)
excluding = wincard[-2::-1]
a = ''
result=0
even = 0
odd = 0

for i in range(0,len(excluding),1):
    a = excluding[i]
    a = int(a)
    if i%2==0:
        a=a*2
        if a<=9:
            even+=a
        elif a>9:
            a-=9
            even+=a
            
    elif i%2==1:
        odd+=a
        
if (odd+even+last1) % 10 ==0:
    print('valid')
else:
    print('invalid')
        
    
    