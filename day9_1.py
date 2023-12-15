file = open("input_day9.txt")
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
    extended_history.append(history)
    while refine:
        for i in range(len(history)-1):
            print(i)
            # print(history)
            dif = history[i+1]-history[i]
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
        extended_history.append(history)
        
    print("EH: ",extended_history)
    for j in range(len(extended_history)-1,-1,-1):
        v1 = extended_history[j][len(extended_history[j])-1]
        v2 = extended_history[j-1][len(extended_history[j-1])-1]
        v3 = v1+v2
        extended_history[j-1].append(v3)
    print(v3)
    summ += v3
    print("EHN:",extended_history)

print("sum:",summ)