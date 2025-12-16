#Oskaras Piskorowski
#15th December 2025
#November Assesment revision

wincard = '8549018035096133'
last1 = wincard[-1]
last1 = int(last1)
excluding = wincard[-2::-1]
result = 0

even_indices = excluding[0::2]
odd_indices = excluding[1::2]

for i in even_indices:
    i = int(i)
    i*=2
    if i>9:
        i-=9
        
    i+=result
        
for j in odd_indices:
    j = int(j)
    j+=j
        
    j+=result
    last1+=result
    
if result%10 ==0:
    print('Valid')
    
else:
    print('Invalid')
        

