#Author Oskaras Piskorowski
#Date 2nd September 2025
#Programme Programme that asks for your height in cm and converts it to feet and inches

heightcm = float(input('Please enter your height in cm: '))

heightinch = heightcm/2.54
heightinch = float(heightinch)

heightfoot = heightinch//12
heightfoot = float(heightfoot)
remainder = heightinch%12

print(heightcm,'cm is',heightfoot,'feet',remainder,'inches')

