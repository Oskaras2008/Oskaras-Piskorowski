#Question 2
#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both
#words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
#OSKARAS PISKOROWSKI
 
string = input("Enter a two word string")
word1 = ' '
word2 = ' '
count = -1
 
 
for i in string:
    word1+=i
    count+=1
    if i == ' ':
        break
word1 = string[0:count]
word2 = string[count+1:]
def animal_crackers(a):
    if word1[0] ==word2[0]:
        a = True
    else:
        a = False
    return a
x = animal_crackers(0)
print(x)
