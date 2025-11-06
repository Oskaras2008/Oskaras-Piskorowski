#Oskaras Piskorowski
#6th of November 2025
#Assignment 12 q 4
#inputs texts and counts the amount of vowels in it

text=input('Enter text: ')
count=0

reversed = text[::-1]
for i in reversed:
    if i =='a' or i =='A' or i =='e' or i =='E' or i =='i' or i =='I' or i =='u' or i =='U' or i =='o' or i =='O':
        count+=1

print(count)