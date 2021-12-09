with open('Day1.txt', "r") as file_input:
    strlines = file_input.read().splitlines()
lines = [int(numeric_string) for numeric_string in strlines]

#Part 1       
Nbincr1 = sum((lines[i-1])<=(lines[i]) for i in range(1,len(lines)))
    
print("Part 1 solution is: %d" % Nbincr1)

#Part 2   
Nbincr2 = sum(sum(lines[i-1:i+2])<sum(lines[i:i+3]) for i in range(1,len(lines)-2))
print("Part 2 solution is: %d" % Nbincr2)