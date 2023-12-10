# Time:      7  15   30
# Distance:  9  40  200

# Time:        35     69     68     87
# Distance:   213   1168   1086   1248

file = open("input_day6.txt")
# time  = []
# distance = []
time = ""
distance = ""
ways_to_win=1

for line in file:
    print(line[:-1])
    shor_line = line[11:-1].split(' ')

    for c in shor_line:
        #print(c)
        if (c.isnumeric() and not line.find("Time") == -1):
            time = time+c
        elif (c.isnumeric() and not line.find("Distance") == -1):
            distance = distance+c

print (time)
print (distance)

wins = 0
for j in range(int(time)+1):
    travel_distnace = j*(int(time)-j)
    if (travel_distnace > int(distance)):
        wins +=1
        print(travel_distnace, j)
ways_to_win *= wins

print(ways_to_win)