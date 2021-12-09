with open('Day9.txt', "r") as file_input:
    strlines = file_input.read().splitlines()
    
#Part 1
def checkngb(strlines,Y,X,Xdirection):
    for k in range(-1,2,2):
        #Check horizontal neighbour
        if Xdirection:
            Xneighbour, Yneighbour= [X+k, Y]
        else:
            Xneighbour, Yneighbour= [X, Y-k]
            
        if Xneighbour>=0 and Xneighbour<len(strlines[Y]) and Yneighbour>=0 and Yneighbour<len(strlines):
            if strlines[Yneighbour][Xneighbour]>strlines[Y][X]:
                Imin = True
            else:
                Imin = False
                break
    return Imin

def Ismin1(strlines,Y,X):
    if checkngb(strlines,Y,X,True) and checkngb(strlines,Y,X,False):
        return int(strlines[Y][X])+1
    else:
        return 0        

Sol1 = sum(Ismin1(strlines,i,j) for i in range(len(strlines)) for j in range(len(strlines[i])))
print(Sol1)


