with open('Day2.txt', "r") as file_input:
    strlines = file_input.read().splitlines()

direction=[line.split(" ") for line in strlines]
depth1 = 0
depth2=0
hori = 0
aim = 0

for direct in direction:
    if direct[0]=="forward":
        hori+=int(direct[1])
        depth2+=aim*int(direct[1])
    elif direct[0]=="down":
        depth1+=int(direct[1])
        aim+=int(direct[1])
    else:
        depth1-=int(direct[1])
        aim-=int(direct[1])

Part1Sol=depth1*hori
Part2Sol=depth2*hori
print("Part 1 solution is: %s" % Part1Sol)
print("Part 2 solution is: %d" % Part2Sol)