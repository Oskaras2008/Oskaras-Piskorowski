#Author Oskaras Piskorowski
#Date 4th September
#Programme that asks user if it is raining if they enter yes ask if its windy if they say yes to that
#then say that it is too windy for an umbrella otherwise display the message take an umbrella and if they said
#no to the first question then say enjoy your day

rainy = input('Is it raining? ')

if rainy == ('yes' or 'Yes'):
        windy = input('is it windy? ')
        if windy == ('yes' or 'Yes'):
            print('It is too windy for an umbrella')         
        else:
            print(' Bring an umbrella')

else:
        print('enjoy your day')
    

    