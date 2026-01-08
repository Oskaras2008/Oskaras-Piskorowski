#Oskaras Piskorowski
#1/8/26



cardno= int(input('Enter your card number'))
counter=1
continueWithCheck = False
cardno = str(cardno)
 
while continueWithCheck ==False and counter<3:
    if len(cardno) ==16:
        continueWithCheck = True
        counter+=1

    elif len(cardno)!=16:
        counter+=1
        cardno = input('That was incorrect, please try again')
        continue
    cardno = int(cardno)
    cardNumber = cardno
    while cardno >10:
        cardno = cardno//10
    if cardno == 7:
        print('This is a ZinCard')
    elif cardno ==8:
        print('This is a WinCard')
    else:
        print('Invalid')
        break
    date = int(input('Enter the card expiry date e.g. 11/26 should be entered as 1126: '))
    total = 0
    while date >10:
        total+=(date%10)
        date = date//10
        if date <10:
            total+=date
    cardNumber = str(cardNumber)
    multiply_number = cardNumber[0:2]
    multiply_number = int(multiply_number)
    subtract_number = cardNumber[9]
    subtract_number = int(subtract_number)
    cvv = (total*multiply_number) - subtract_number
    print('CVV:',cvv)
    the_card_number = cardNumber[0:4] + '-' + cardNumber[4:8] + '-' +cardNumber[8:12] + '-' + cardNumber[12::]
    print(the_card_number)