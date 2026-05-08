#Question 1
#LESSER OF TWO EVENS: Write a function that returns the lesser of two given
#numbers if both numbers are even, but returns the greater if one or both numbers are
#odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
#OSKARAS PISKOROWSKI

def lesser_of_two_evens(a,b):
    n = 0
    if a%2 == 0 and b%2 == 0:
        if a>b:
            n=b
        elif b>a:
            n=a
    elif a%2 == 1 or b%2 == 1:
        if a>b:
            n = a
         
        elif b>a:
            n = b
    return n

x = lesser_of_two_evens(64,167)
print(x)

