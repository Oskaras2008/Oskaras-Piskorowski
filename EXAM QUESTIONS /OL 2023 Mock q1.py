#Oskaras Piskorowski
#ExamCraft OL
#3.13.26

count = 0
option = input('Would you like to (a)dd, (s)ubtract, (m)ultiply , or (d)ivide? ')
num1 = float(input('Please enter your first number: '))
num2 = float(input('Please enter your second number: '))

if option == 'a':
    answer = num1+num2
    answer = str(answer)
    for i in answer:
        count+=1
        if i =='.':
            abc =answer[0:count]       
            print(num1,'+',num2, '=' ,answer)
            
if option == 's':
    answer = num1-num2
    answer = str(answer)
    for i in answer:
        count+=1
        if i =='.':
            abc =answer[0:count]       
            print(num1,'-',num2, '=' ,answer)
if option == 'm':
    answer = num1*num2
    answer = str(answer)
    for i in answer:
        count+=1
        if i =='.':
            abc =answer[0:count]       
            print(num1,'*',num2, '=' ,answer)
if option == 'd':
    answer = num1/num2
    answer = str(answer)
    for i in answer:
        count+=1
        if i =='.':
            abc =answer[0:count]       
            print(num1,'/',num2, '=' ,answer)

