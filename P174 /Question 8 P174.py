#Author Oskaras Piskorowski
#Date 2nd September 2025
#Programme Programme that asks for your height in cm and converts it to feet and inches

heightcm = int(input('Please enter your height in cm: '))

heightinch = heightcm/2.54
heightinch = int(heightinch)

heightfoot = heightinch//12
heightfoot = int(heightfoot)
remainder = heightinch%12

print(heightcm,'cm is',heightfoot,'feet',remainder,'inches')
