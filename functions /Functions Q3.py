#Question 3
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one
#of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
#OSKARAS PISKOROWSKI

def makes_twenty(a,b):
    if a ==20 or b==20:
        c = True
    elif a+b ==20:
        c = True
    else:
        c = False
        
    return a,b,c

x= makes_twenty(67,-47)
print(x[2])
        
        
        










