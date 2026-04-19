#Oskaras Piskorowski
#7th of November 2025
#Assignment 12 q 1
#Roman Numerals
number = int(input('Enter a number less than 5000'))
roman_numerals = ''

if number>=5000:
    print('LESS THAN 5000')
while (number>=1000) and (number<5000):
    roman_numerals+='M'
    number-=1000
    
while (number>=900) and (number<1000):
    roman_numerals+='CM'
    number-=900
    
while (number>=800) and (number<900):
    roman_numerals+='DCCC'
    number-=800
    
while (number>=700) and (number<800):
    roman_numerals+='DCC'
    number-=700
    
while (number>=600) and (number<700):
    roman_numerals+='DC'
    number-=600
    
while (number>=500) and (number<600):
    roman_numerals+='D'
    number-=500
    
while (number>=400) and (number<500):
    roman_numerals+='D'
    number-=400
    
while (number>=300) and (number<400):
    roman_numerals+='CCC'
    number-=300
    
while (number>=200) and (number<300):
    roman_numerals+='CC'
    number-=200
    
while (number>=100) and (number<200):
    roman_numerals+='C'
    number-=100
    
while (number>=90) and (number<100):
    roman_numerals+='XC'
    number-=90
    
while (number>=80) and (number<90):
    roman_numerals+='LXXX'
    number-=80
    
while (number>=70) and (number<80):
    roman_numerals+='LXX'
    number-=70
    
while (number>=60) and (number<70):
    roman_numerals+='LX'
    number-=60
    
while (number>=50) and (number<60):
    roman_numerals+='L'
    number-=50
    
while (number>=40) and (number<50):
    roman_numerals+='XL'
    number-=40
    
while (number>=30) and (number<40):
    roman_numerals+='XXX'
    number-=30
    
while (number>=20) and (number<30):
    roman_numerals+='XX'
    number-=20
    
while (number>=10) and (number<20):
    roman_numerals+='X'
    number-=10
    
while (number>=9) and (number<10):
    roman_numerals+='IX'
    number-=9
    
while (number>=8) and (number<9):
    roman_numerals+='VIII'
    number-=8
    
while (number>=7) and (number<8):
    roman_numerals+='VII'
    number-=7
    
while (number>=6) and (number<7):
    roman_numerals+='VI'
    number-=6
    
while (number>=5) and (number<6):
    roman_numerals+='V'
    number-=5
    
while (number>=4) and (number<5):
    roman_numerals+='IV'
    number-=4
    
while (number>=3) and (number<4):
    roman_numerals+='III'
    number-=3
    
while (number>=2) and (number<3):
    roman_numerals+='II'
    number-=2
    
while (number>=1) and (number<2):
    roman_numerals+='I'
    number-=1
    
print(roman_numerals)
    
    
