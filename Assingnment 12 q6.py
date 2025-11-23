#Oskaras Piskorowski
#20th November 2025
#Assignment 12 q 6
#Reverse each word in a string
 
string = input('Enter a string : ')
substring = ' '
result = ' '

count = 0
a = 0
for i in string:
    count+=1
    if i == ' ':
        substring= string[count -1::-1]
        result+=substring
        string = string[count:len(string)]
        count=0
      
print(result,string[::-1])

