import statistics
with open('Day10.txt', "r") as file_input:
    strlines = file_input.read().splitlines() 

def removechunk(line,modif):
    modif=False
    brackets = [["(",")"],["[","]"],["{","}"],["<",">"]]
    for bracket in brackets:
        chunk = bracket[0]+bracket[1]
        while chunk in line:
            line=line.replace(chunk,"")
            modif=True
    return line,modif

brack_out = [[")","]","}",">"],[3,57,1197,25137]]
brack_in = [["(","[","{","<"],[1,2,3,4]]
def countillchar(line,part,incompletes_value=[], modif =True,middle ="", illegal =0):
    while modif == True:
        line,modif = removechunk(line,modif)
    for char in line:
         if char in brack_out[0]:
             illegal = brack_out[1][brack_out[0].index(char)]
             break
    if part == 1:
        return illegal
    elif part ==2 and illegal==0:
        for char in reversed(line):
            illegal = illegal*5 + brack_in[1][brack_in[0].index(char)]
        incompletes_value.append(illegal)
        middle = statistics.median(incompletes_value)
        return middle

Sol1 =  sum(countillchar(line,1) for line in strlines)
print(f"Solution of part 1 is: {Sol1}")

for line in strlines:
    Sol2 = countillchar(line,2)
print(f"Solution of part 2 is: {Sol2}")
