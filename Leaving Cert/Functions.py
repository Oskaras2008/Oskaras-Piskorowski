

def mean(list):
    total = 0
    x= 0
    for i in list:
        x+=1
        total+=i
        
    mean = total//x
        
    return mean

    
def med(list):
    length = len(list)
    length = int(length)
    list.sort()
    if length%2 == 1:
        med = list[((length)//2)]
    elif length%2 ==0:
        med = (list[((length//2))-1]+list[((length//2))])/2
    return med


def mode(list):
    maxi = 0
    count = 0
    mode = list[0]
    for i in list:
        if list.count(mode) < list.count(i) :
            maxi = list.count(i)
            mode = i
        else:
            continue
    return mode

def frequency(list):
    list.sort()
    n = [ ]
    frq = [ ]
    count = 0
    
    for i in list:
        if i not in n:
            n.append(i)
            count=list.count(i)
            
            
    return frequency,n,frq

def range(list):
    
    f = max(list) - min(list)
    return f


            
    


list = eval(input("Enter a list of numbers: "))
y = mean(list)
print("mean:",y)

z = med(list)
print("median:",z)

q = mode(list)
print("mode:",q)

v = frequency(list)
for i in list:
    print('The frequency of',i,'is',v)
    
e = range(list)
print('The range is:',e)


        