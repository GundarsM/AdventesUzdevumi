from random import choice
from string import ascii_lowercase
from sklearn import metrics 

file = open("input3.txt")

line_list = []

for line in file:
    line_len=len(line)

    line_list.append(line[:len(line)-1])

string_val = "".join('·' for i in range(line_len))

line_list.insert(0,string_val)
line_list.append(string_val)

for i in range(len(line_list)-2):
    for line in line_list:
        for letter in line:
            #print(letter)
            if ((ord(letter) > 32) and (ord(letter) < 48) and (ord(letter) > 57) and not (ord(letter) ==46)):
                print(letter,end="")


print((line_list))