import sys

file = open("input_day9_t.txt")
all_history = []

for line in file:
    current_history =[]
    numbers = line[:-1].split(' ')
    for number in numbers:
        current_history.append(int(number))

        
    all_history.append(current_history)

# print(all_history)

summ = 0
for history in all_history:
    extended_history = []
    next_history =[]
    sum = 0
    refine = 1
    extended_history.append([history[-1]])
    while refine:
        for i in range(len(history)-1):
            # print(i)
            # print(history)
            dif = abs(history[i+1]-history[i])
            sum+=dif
            next_history.append(dif)
            # if (len(next_history)==(len(history)-1)):
            #     refine = 0
            
            # print(i,sum, len(next_history)-1, len(history)-1, next_history)

        if sum == 0:
            # print("BBB")
            history = next_history.copy()
            refine = 0
            

        if sum > 0:
            # print("AAA")
            history = next_history.copy()
            next_history.clear()
            sum = 0
            
        
        # print("CCC")
        # print("H:", history)
        # print("NH:", history)

        if len(history)==0:
            # print("empty")
            extended_history.append([0])
        else:
            extended_history.append([history[-1]])
        # value = input("Please enter a string:\n")
    # print("EH: ",extended_history)
    for j in range(len(extended_history)-1,0,-1):
        v1 = extended_history[j][-1]
        v2 = extended_history[j-1][-1]
        if v2<0:
            v3 = v2-v1
        else:
            v3 = v1+v2
        # print("v3-1",v3,v2,v1)
        if j == len(extended_history)-1:
            # print("aaa")
            extended_history[j].append(v1)
            extended_history[j-1].append(v3)
        else:
            # print("bbb")
            extended_history[j-1].append(v3)
        # print("EHN_:",extended_history)
    # print("v3",v3)

    summ += v3
    print("EHN:",extended_history)
    # value = input("Please enter a string:\n")
print("sum:",summ)
if summ>100:
    sys.exit(1)