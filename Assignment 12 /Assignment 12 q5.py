#Oskaras Piskorowski
#6th of November 2025
#Assignment 12 q 5
#inputs texts and prints the biggest word
text=input('Enter text: ')
count=0
biggest = ''

for i in text:
    if i==' ':
        if len(biggest)<len(text[count:text.index(i)]):
            biggest+=text[count:text.index(i)]
            count+=text.index(i)
            
print(biggest)
        
        

        

    
