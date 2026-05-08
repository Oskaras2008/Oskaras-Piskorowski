#OSKARAS PISKOROWSKI
 
values = [ ]
c = 1
avg = 0
a = 0
count = 0
l = [ ]
#----------------------------------------------------------------------
while c != 0000:
    c = int(input('Enter a list of values and input 0 to end: ' ))
    if c==0:
        break
    values.append(c)
    a+=1
print(values)
#----------------------------------------------------------------------
def range(j):
    #maxi = max(l)
    #mini = min(l)
    f = max(h) - min(h)
    return f
h = values
e = range(values)
print('The range is:',e)
#----------------------------------------------------------------------
def average(b):
    sum1 = sum(l)
    avg = sum1/count
    return avg
l = values
count = a
d = average(values)
print('The average is',d)
#----------------------------------------------------------------------
 
def median(q):
    length = len(q)
    length = int(length)
    q.sort()
    if length%2 == 1:
        median = q[((length)//2)]
    elif length%2 ==0:
        median = (q[((length//2))-1]+q[((length//2))])/2
    return median
q = values
v = median(q)
print('The median is',v)
 
#----------------------------------------------------------------------

maximum = 0
 
def mode(vv):
    mode = vv[0]
    for i in vv:
        if vv.count(mode) < vv.count(i):
            maximum = vv.count(i)
            mode = i
        else:
            continue
    return mode
vv = values
op = mode(vv)
print('The mode is',op)

#----------------------------------------------------------------------

use = [ ]
freq = [ ]
count = 0

def frequency(freq):
    for i in oo:
        if i not in use:
            use.append(i)
            count = oo.count(i)
            print('The frequency of',i,'is',count)
    return freq, use
oo = values
rr = frequency(oo)

 
            

