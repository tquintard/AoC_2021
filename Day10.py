with open('Day10.txt', "r") as file_input:
    strlines = file_input.read().splitlines() 

#Part 1
def removechunk(line,modif):
    templine=""
    modif=False
    newline=line
    brackets = [["(",")"],["[","]"],["{","}"],["<",">"]]
    for bracket in brackets:
        chunk = bracket[0]+bracket[1]
        while chunk in newline:
            templine=newline.replace(chunk,"")
            newline = templine
            templine=""
            modif=True
    return newline,modif

# brack_in = ["(","[","{","<"]

def countillchar(line):
    brack_out = [[")","]","}",">"],[3,57,1197,25137]]
    modif = True
    myline = line
    illpoint = 0
    while modif == True:
        myline,modif = removechunk(myline,modif)
    for char in myline:
         if char in brack_out[0]:
             illpoint = brack_out[1][brack_out[0].index(char)]
             break
    return illpoint

Sol1 =  sum(countillchar(line) for line in strlines)
print(Sol1)