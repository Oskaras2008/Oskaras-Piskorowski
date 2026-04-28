#Question 16(a)
#Name and School

choice = str(input("Enter 1 for fahrenheit to celsius or Enter 2 for celsius to fahrenheit"))
if choice == '1':
    
    fahrenheit = float(input("Enter a temperature in degrees fahrenheit"))
    
    def fahrenheit_to_celcius(fahrenheit):
        celsius = (fahrenheit * 5/9) - 32
        return celsius

    rounded1 = round(fahrenheit_to_celcius(fahrenheit),2)
    
    k = rounded1+273.15
    print(fahrenheit,chr(176),"F" ," is equal to",rounded1,chr(176),"C" "  and",k,"K")
    
elif choice == '2':
    
    celsius = float(input("Enter a temperature in degrees celsius"))

    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    rounded = round(celsius_to_fahrenheit(celsius),2)
    k = celsius+273.15
    print(celsius,chr(176),"C" ," is equal to",rounded,chr(176),"F" "  and",k,"K")
