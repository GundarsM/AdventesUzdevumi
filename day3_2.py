from random import choice
from string import ascii_lowercase
import string
import re

file = open("input_day3.txt")

line_list = []

for line in file:
    line_len=len(line)+2
    line_list.append('.'+ line[:len(line)-1] + '.')
    #line_list.insert()

#print (line_list)
#print (line_len)
 
string_val = "".join('.' for i in range(line_len))
line_list.insert(0,string_val)
line_list.append(string_val)

print((line_list))
total_sum=0
for i in range(1,len(line_list)-1):
    result = re.findall(r'\d+',line_list[i])
    #print(result)
    for j in range(len(result)):
        serch = re.search(str(result[j]),line_list[i])
        #print(result[j],end=" ")
        #print(serch)
        if serch:
            #print(serch.start())
            if serch.span()[1]-serch.span()[0]==3:
                print(result[j])
                for ii in range(-1,4):      #elements rindā
                    for jj in range(-1,2):  #rinda                      
                        if not ((ii>-1 and ii<3) and (jj==0)):
                            symbol = line_list[i+jj][serch.start()+ii]

                            # if result[j]=='30' or result[j]=='295':
                            #     print(serch)
                            #     print(i+jj,serch.start()+ii)
                            #     print(symbol) 

                            if not (symbol == '.') and not (ord(symbol) < 57 and ord(symbol) > 48):
                                print(symbol)  #[rinda][elements rindā]
                                #print('z')#line_list[jj][ii])
                                total_sum += int(result[j])
                        #else:
                            #line_list[i+jj][serch.start()+ii]='.' 
                new_string = line_list[i][:serch.start()] + '...' + line_list[i][serch.start()+3:]
                #print(line_list[i])
                #print(new_string)
                line_list[i] = new_string
                #print(line_list[i])

            elif serch.span()[1]-serch.span()[0]==2:
                print(result[j])
                for ii in range(-1,3):      #elements rindā
                    for jj in range(-1,2):  #rinda                    
                        if not ((ii>-1 and ii<2) and (jj==0)):
                            #print(line_list[i-jj][serch.start()+ii])  #[rinda][elements rindā]
                            symbol = line_list[i+jj][serch.start()+ii]
                            
                            # if result[j]=='30' or result[j]=='295':
                            #     print(serch)
                            #     print(i+jj,serch.start()+ii)
                            #     print(symbol)  
                            if not (symbol == '.') and not (ord(symbol) < 57 and ord(symbol) > 48):
                                print(symbol)  #[rinda][elements rindā]
                                #print('z')#line_list[jj][ii])
                                total_sum += int(result[j])
                new_string = line_list[i][:serch.start()] + '..' + line_list[i][serch.start()+2:]
                #print(line_list[i])
                #print(new_string)
                line_list[i] = new_string

            elif serch.span()[1]-serch.span()[0]==1:
                print(result[j])
                for ii in range(-1,2):      #elements rindā
                    for jj in range(-1,2):  #rinda                      
                        if not ((ii>-1 and ii<1) and (jj==0)):
                            #print(line_list[i-jj][serch.start()+ii])  #[rinda][elements rindā]
                            symbol = line_list[i-jj][serch.start()+ii]
                            if not (symbol == '.') and not (ord(symbol) < 57 and ord(symbol) > 48):
                                print(line_list[i-jj][serch.start()+ii])  #[rinda][elements rindā]
                                #print('z')#line_list[jj][ii])
                                total_sum += int(result[j])
                new_string = line_list[i][:serch.start()] + '.' + line_list[i][serch.start()+1:]
                #print(line_list[i])
                #print(new_string)
                line_list[i] = new_string

            else:
                serch.span()[1]-serch.span()[0]>3
                print(result[j])
                print("MORE")
            
            

print(total_sum)
    # for line in line_list:
    #     for letter in line:
    #         #print(letter)
    #         if ((ord(letter) > 32) and (ord(letter) < 48) and (ord(letter) > 57) and not (ord(letter) ==46)):
    #             #print(letter,end="")

