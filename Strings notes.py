'''variable1= 'This string'\
' goes over'\
' many'\
' lines'
print(variable1)'''

#backslash prints the strings on the same line
#or you can enclose it in brackets

'''variable1= ('This string'
' goes over'
' many'
' lines')
print(variable1)'''

#multiline string
'''variable1= """This string
 goes over
 many
 lines"""
print(variable1)'''

#String addition concatenation
'''fruit = 'ap'+'ple'
print(fruit)'''

#String multiplication(repetition)
'''random_word = 'He'
print(random_word*3)'''

#casting strings
#convert strings to numbers

'''variable1 = '12'
variable2 = '12.3'

print(int(variable1))
print(float(variable2))'''

#You can convert numbers into strings by using str()
'''variable3 = 12
variable4 = 12.3
print(str(variable3))
print(str(variable4))'''

variable5 = 'Hello World!'
#prints the letter 'e' with index positioning 1
'''print(variable5[1])
#Prints the letter 'e ' with index position -11
print(variable5[-11])'''

#To find the number of characters in a string you can use the len() function

'''variable6 = 'apple'
print(len(variable6))'''

#For loop with string
'''variable7 = 'apple'
for i in variable7:
    print(i)'''

#While loop in a string
variable8 = 'apple'
index = 0
while index< len(variable8):
    letter=variable8[index]
    print(letter)
    index=index+1
