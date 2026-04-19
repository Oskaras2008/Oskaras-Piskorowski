#Oskaras Piskorowski
#14th October 2025
# 1**2 +3**2 + 52 +...+ n² (Input n)

n=int(input('Enter a number'))
count=0
for i in range(1,n+1,2):
    count+=i**2
 
print(count)
