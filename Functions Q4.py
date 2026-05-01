#Question 4
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a
#name. If the name is too short it should return an error number
#old_macdonald('macdonald') --> MacDonald
#OSKARAS PISKOROWSKI


name = "ryan"
newname = ' '
def old_macdonald(name,newname):
    length=len(name)
    
    for i in range(0,length):
        if len(name)<4:
            print("ERROR67---NOT ENOUGH LETTERS")
            break
        if i ==0:
            newname+=name[i].upper()
        elif i ==3:
            newname+=name[i].upper()
        elif i !=0 or i !=3:
            newname+=name[i].lower()
        
    return name,newname

x = old_macdonald(name,newname)

print(x[1])
        
    
    
    