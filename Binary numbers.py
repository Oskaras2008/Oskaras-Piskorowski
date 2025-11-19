#Binary adder
#Oskaras Piskorowski
#17th November 2025
 
binary = input('Enter a binary number')
binary_two = input('Enter another binary number')
count = 0
reverse_binary = binary[::-1]
reversebinary_two = binary_two[::-1]
string = ''
longer = 0
length_of_reverse_binary = len(reverse_binary)
length_of_reversebinary_two = len(reversebinary_two)

if length_of_reverse_binary> length_of_reversebinary_two:
    longer = reverse_binary
    shorter = reversebinary_two
    
elif length_of_reverse_binary< length_of_reversebinary_two:
    longer = reversebinary_two
    shorter = reverse_binary

else:
    longer =reverse_binary
    shorter = reversebinary_two
carry = 0

for i in longer:
    i = int(i)
    if  count <len(shorter):
        add = shorter[count]
        add = int(add)
    else:
        add = 0
    sum = i+add+carry
    carry = 0

    if sum >=2:
        sum = sum-2
        sum = str(sum)
        string+=sum
        carry =1
        count+=1

    elif sum <2:
        sum = str(sum)
        string+=sum
        count+=1
 
if carry ==1:
    string+='1'

answer = string[::-1]

print(answer)
 

    





        
    
        
        

