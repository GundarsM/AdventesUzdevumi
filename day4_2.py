from random import choice
from string import ascii_lowercase
from sklearn import metrics 

file = open("input_day4.txt")

total_worth=0
wins_on_card = []

original_cards =[]

for line in file:
    line = line[:-1]
    line = line.split(':')
    line = line[1].split('|')

    win_strings = line[0].split(' ')
    test_strings = line[1].split(' ')

    win_numbers = []
    test_numbers = []
    original_cards.append((win_numbers,test_numbers))
    for i in range(len(win_strings)):
        if not win_strings[i]=='':
            win_numbers.append(int(win_strings[i]))
    
    for i in range(len(test_strings)):
        if not test_strings[i]=='':
            test_numbers.append(int(test_strings[i]))


    #print(win_numbers, end=" ")
    #print(test_numbers)


    worth = 0
    counter = 0
    for i in range(len(win_numbers)):        
        for j in range(len(test_numbers)):
            if win_numbers[i] == test_numbers[j]:
                counter += 1
  
    wins_on_card.append(counter)

#print(wins_on_card)

card_count = len(wins_on_card)

copy_wins =[]
ccopy_wins =[]
for i in range(len(wins_on_card)):
    copy_wins.append(0)
    ccopy_wins.append(0)

#print(copy_wins)


for i in range(len(wins_on_card)):
    for j in range(wins_on_card[i]):
        copy_wins[i+j+1] += 1 

print(copy_wins)

for i in range(len(copy_wins)):
    card_count +=copy_wins[i]

countsss =0
while not sum==0:    
    for i in range(len(wins_on_card)):
        if not copy_wins[i]==0: 
            for j in range(copy_wins[i]):
                for k in range(wins_on_card[i]):
                    ccopy_wins[i+k+1] += 1   
    sum = 0
    for i in range(len(wins_on_card)):
        sum += ccopy_wins[i]
    card_count += sum
    
    copy_wins = ccopy_wins[:]
    print(sum)
    for i in range(len(wins_on_card)):
        ccopy_wins[i]=0

    print(copy_wins) 
    countsss +=1

print (card_count)

