
list_1 = [4, 5, 9, 8, 10, 17, 99, 77]

list_1.sort()  
n = len(list_1)

if n % 2 != 0:

    median = list_1[n // 2]
else:
    mid1 = list_1[n // 2 - 1]
    mid2 = list_1[n // 2]
    median = (mid1 + mid2) / 2

print("The median is:", median)
