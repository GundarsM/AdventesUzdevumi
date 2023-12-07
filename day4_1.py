from random import choice
from string import ascii_lowercase
from sklearn import metrics 

file = open("input_day4.txt")

total_worth=0
for line in file:
    line = line[:-1]
    line = line.split(':')
    line = line[1].split('|')

    win_strings = line[0].split(' ')
    test_strings = line[1].split(' ')

    win_numbers = []
    test_numbers = []

    for i in range(len(win_strings)):
        if not win_strings[i]=='':
            win_numbers.append(int(win_strings[i]))
    
    for i in range(len(test_strings)):
        if not test_strings[i]=='':
            test_numbers.append(int(test_strings[i]))


    print(win_numbers, end=" ")
    print(test_numbers)


    worth = 0
    counter = 0
    for i in range(len(win_numbers)):        
        for j in range(len(test_numbers)):
            if win_numbers[i] == test_numbers[j]:
                counter += 1
  
    if(counter):
        worth = pow(2,counter-1)
        print(pow(2,counter-1))
    else:
        worth = 0
        print(0)

    total_worth += worth

print(total_worth)
