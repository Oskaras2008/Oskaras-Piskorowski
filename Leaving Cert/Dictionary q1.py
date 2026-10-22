
def freq(a):
    b = a.casefold()
    newword = " "
    used_list = [ ]
    list = [ ]
    count = 0
    dict1 = { }
    for i in b:
        if i != " ":
            newword+=i      
        elif i == " ":
            list.append(newword)
            newword = " "
    list.append(newword)
    
    #dict1={'Word','Count'}
    for x in list:
        if x not in dict1:
            dict1[x] = 1
        elif x in dict1:
            dict1[x] = dict1[x] + 1
            
    return dict1
            
def frequency(d):
    b = d.casefold()
    newlet = " "
    used_list = [ ]
    list = [ ]
    count = 0
    dict2 = { }
    for i in b:
        if i != " ":
            used_list+=i      
        #elif i == " ":
            continue
    
    #dict1={'Word','Count'}
    for x in used_list:
        if x not in dict2:
            dict2[x] = 1
        elif x in dict2:
            dict2[x] = dict2[x] + 1
             
    return dict2

choice =int(input("Enter 1 to count letters in a sentence and enter 2 to count words in a sentence:"))
if choice == 1 :
    d = str(input("Enter a sentence"))
    c = frequency(d)
    print(c)
elif choice == 2 :
    a = str(input("Enter a sentence"))
    e = freq(a)
    print(e)
else:
    print("Enter again")


        
            
            
