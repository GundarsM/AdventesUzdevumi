import re
import array as arr
import numpy as np

file = open("input_day5.txt")
count = 0
read_seed_to_soil = 0
read_soil_to_fertilizer = 0
read_fertilizer_to_water = 0
read_water_to_light = 0
read_light_to_temperature = 0
read_temp_to_hum = 0
read_humt_to_location = 0

seed = []
seed_to_soil =[]
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_locat = []

print("read input")
for line in file:
    #print(line[:-1])
    if count == 0:
        seed = [int(s) for s in line.split() if s.isdigit()]# re.findall(r'\d+',line)
    
    count +=1

    if (count > 1 and line.find("seed-to-soil") != -1):
        read_seed_to_soil = 1
        continue

    if (count > 1 and line.find("soil-to-fertilizer") != -1):
        read_soil_to_fertilizer = 1
        read_seed_to_soil = 0
        continue

    if (count > 1 and line.find("fertilizer-to-water") != -1):
        read_fertilizer_to_water = 1
        read_soil_to_fertilizer = 0
        continue

    if (count > 1 and line.find("water-to-light") != -1):
        read_water_to_light = 1
        read_fertilizer_to_water = 0
        continue

    if (count > 1 and line.find("light-to-temperature") != -1):
        read_light_to_temperature = 1
        read_water_to_light = 0
        continue

    if (count > 1 and line.find("temperature-to-humidity") != -1):
        read_temp_to_hum = 1
        read_light_to_temperature = 0
        continue
    
    if (count > 1 and line.find("humidity-to-location") != -1):
        read_humt_to_location = 1
        read_temp_to_hum = 0
        continue

    

    if read_seed_to_soil:
        if len(line)>1:
            seed_to_soil.append([int(s) for s in line.split() if s.isdigit()])

    if read_soil_to_fertilizer:
        if len(line)>1:
            soil_to_fert.append([int(s) for s in line.split() if s.isdigit()])
    
    if read_fertilizer_to_water:
        if len(line)>1:
            fert_to_water.append([int(s) for s in line.split() if s.isdigit()])

    if read_water_to_light:
        if len(line)>1:
            water_to_light.append([int(s) for s in line.split() if s.isdigit()])

    if read_light_to_temperature:
        if len(line)>1:
            light_to_temp.append([int(s) for s in line.split() if s.isdigit()])

    if read_temp_to_hum:
        if len(line)>1:
            temp_to_hum.append([int(s) for s in line.split() if s.isdigit()])

    if read_humt_to_location:
        if len(line)>1:
            hum_to_locat.append([int(s) for s in line.split() if s.isdigit()])

#create seed to soil list

#print(seed_to_soil)
# source - seed
# destination - soil

#get max seed number

print("create seed list")




new_max = 0
for i in range(len(seed_to_soil)):
    test = (seed_to_soil[i][1]+seed_to_soil[i][2]-1)
    if test > new_max: new_max = test

print(new_max)


seed_array = np.empty(new_max+1,int)

#print(seed_array)

# seed_list = []
for i in range(new_max+1):
    # seed_list.append(i)
    seed_array[i]=str(i)
    #print(i, new_max)

# print(seed_array)
#print(seed_list)

# print(len(seed_list))
# print(len(soil_list))


print("create soil list")

# for i in range(len(seed_to_soil)):
#     for j in range(seed_to_soil[i][2]):
#         soil_list[seed_to_soil[i][1]+j] = seed_to_soil[i][0]+j

soil_array = np.copy(seed_array)

#print(soil_array)

# soil_list =[]
# soil_list = seed_list[:]

for i in range(len(seed_to_soil)):              # 3x
    #print(soil_to_fert[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x 
    while (k <= new_max) and counteris < seed_to_soil[i][2]: 
        k+=1     
        if k > new_max: 
            k=0   
            #print("ops")
        #if seed_list[k] == seed_to_soil[i][1]+counteris:  # ja ir 15
        if seed_array[k] == seed_to_soil[i][1]+counteris:
            soil_array[k] = seed_to_soil[i][0]+counteris
            # soil_list[k] = seed_to_soil[i][0]+counteris   # tad fert 15 = 0
            #print(k, fert_list[k], counteris, soil_to_fert[i][0]+counteris)
            counteris += 1                        
            if k == new_max and counteris < seed_to_soil[i][2]-1:
                #print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0                  
            if counteris > seed_to_soil[i][2]: break 

#print(soil_list)
# print(soil_array)

# print(soil_list)

# fert_list = []
print("create fert list")
# fert_list = soil_list[:]

fert_array = np.copy(soil_array)

for i in range(len(soil_to_fert)):              # 3x
    #print(soil_to_fert[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x 
    while (k <= new_max) and counteris < soil_to_fert[i][2]: 
        k+=1  
        #print(k,new_max)   
        if k > new_max: 
            k=0   
            # print("ops")
        #if soil_list[k] == soil_to_fert[i][1]+counteris:  # ja ir 15   
        if soil_array[k] == soil_to_fert[i][1]+counteris:
            # fert_list[k] = soil_to_fert[i][0]+counteris   # tad fert 15 = 0
            fert_array[k] = soil_to_fert[i][0]+counteris
            #print(k, fert_list[k], counteris, soil_to_fert[i][0]+counteris)
            counteris += 1                        
            if k >= new_max and counteris < soil_to_fert[i][2]-1:
                # print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0                  
            if counteris > soil_to_fert[i][2]: break          

# print(fert_list)
# print(fert_array)

# water_list = []
water_array = np.copy(fert_array)

print("create water list")
# water_list = fert_list[:]

for i in range(len(fert_to_water)):              # 3x
    #print(fert_to_water[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x  
    while (k <= new_max) and counteris < fert_to_water[i][2]:    # 100x
        k+=1    
        if k > new_max: 
            k=0   
            # print("ops")
        #print(k, len(seed_list)-1, fert_list[k],fert_to_water[i][1]+counteris, fert_to_water[i][2]-1, counteris)
        #if fert_list[k] == fert_to_water[i][1]+counteris:  # ja ir 49
        if fert_array[k] == fert_to_water[i][1]+counteris:
            water_array[k] = fert_to_water[i][0]+counteris 
            # water_list[k] = fert_to_water[i][0]+counteris   # tad fert 15 = 0
            #print(k, water_list[k], counteris, fert_to_water[i][0]+counteris)
            counteris += 1            
                           
            if k >= new_max  and counteris < fert_to_water[i][2]-1:
                #print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0
            if counteris > fert_to_water[i][2]-1: break
            

# print(water_list)
# print(water_array)

# light_list = []
print("create light list")
light_array = np.copy(water_array)
# light_list = water_list[:]

for i in range(len(water_to_light)):              # 3x
    #print(fert_to_water[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x  
    while (k <= new_max) and counteris < water_to_light[i][2]:    # 100x
        k+=1    
        if k> new_max:
            k=0   
            #print("ops")
        #print(k, len(seed_list)-1, fert_list[k],fert_to_water[i][1]+counteris, fert_to_water[i][2]-1, counteris)
        #if water_list[k] == water_to_light[i][1]+counteris:  # ja ir 49
        if water_array[k] == water_to_light[i][1]+counteris:
            # light_list[k] = water_to_light[i][0]+counteris   # tad fert 15 = 0
            light_array[k] = water_to_light[i][0]+counteris
            #print(k, water_list[k], counteris, fert_to_water[i][0]+counteris)
            counteris += 1            
                        
            if k >= new_max and counteris < water_to_light[i][2]-1:
                #print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0
            if counteris>water_to_light[i][2]-1: break   
            

# print(light_list)
# print(light_array)
# temp_list = []
print("create temp list")
temp_array = np.copy(light_array)

# temp_list = light_list[:]

for i in range(len(light_to_temp)):              # 3x
    #print(fert_to_water[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x  
    while (k <= new_max) and counteris < light_to_temp[i][2]:    # 100x
        k+=1    
        if k> new_max: 
            k=0   
            #print("ops")
        #print(k, len(seed_list)-1, fert_list[k],fert_to_water[i][1]+counteris, fert_to_water[i][2]-1, counteris)
        #if light_list[k] == light_to_temp[i][1]+counteris:  # ja ir 49
        if light_array[k] == light_to_temp[i][1]+counteris: 
            temp_array[k] = light_to_temp[i][0]+counteris 
            # temp_list[k] = light_to_temp[i][0]+counteris   # tad fert 15 = 0
            #print(k, water_list[k], counteris, fert_to_water[i][0]+counteris)
            counteris += 1            
                          
            if k >= new_max and counteris < light_to_temp[i][2]-1:
                #print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0
            if counteris>light_to_temp[i][2]-1: break 

# print(temp_list)
# print(temp_array)

# hum_list = []
print("create hum list")
# hum_list = temp_list[:]
hum_array = np.copy(temp_array)

for i in range(len(temp_to_hum)):              # 3x
    #print(fert_to_water[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x  
    while (k <= new_max) and counteris < temp_to_hum[i][2]:    # 100x
        k+=1    
        if k> new_max: 
            k=0   
            #print("ops")
        #print(k, len(seed_list)-1, fert_list[k],fert_to_water[i][1]+counteris, fert_to_water[i][2]-1, counteris)
        #if temp_list[k] == temp_to_hum[i][1]+counteris:  # ja ir 49
        if temp_array[k] == temp_to_hum[i][1]+counteris:
            # hum_list[k] = temp_to_hum[i][0]+counteris   # tad fert 15 = 0
            hum_array[k] = temp_to_hum[i][0]+counteris
            #print(k, water_list[k], counteris, fert_to_water[i][0]+counteris)
            counteris += 1            
                        
            if k >= new_max and counteris < temp_to_hum[i][2]-1:
                #print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0
            if counteris>temp_to_hum[i][2]-1: break   

# print(hum_list)
# print(hum_array)

print("create loc list")

loc_array = np.copy(hum_array)

for i in range(len(hum_to_locat)):              # 3x
    #print(fert_to_water[i])   
    counteris = 0 
    k = 0
    #for k in range(len(seed_list)):             # 100x  
    while (k <= new_max) and counteris < hum_to_locat[i][2]:    # 100x
        k+=1    
        if k> new_max: 
            k=0   
            #print("ops")
        #print(k, len(seed_list)-1, fert_list[k],fert_to_water[i][1]+counteris, fert_to_water[i][2]-1, counteris)
        #if hum_list[k] == hum_to_locat[i][1]+counteris:  # ja ir 49
        if hum_array[k] == hum_to_locat[i][1]+counteris: 
            loc_array[k] = hum_to_locat[i][0]+counteris
            #print(k, water_list[k], counteris, fert_to_water[i][0]+counteris)
            counteris += 1            
                       
            if k >= new_max and counteris < hum_to_locat[i][2]-1:
                #print("oops")
                #print(k,len(seed_list)-1 , counteris,fert_to_water[i][2]-1)
                k=0
            if counteris>hum_to_locat[i][2]-1: break    

# print(loc_array)


pritn_val = 79
print(seed_array[pritn_val], end=" ")
print(soil_array[pritn_val], end=" ")
print(fert_array[pritn_val], end=" ")
print(water_array[pritn_val], end=" ")
print(light_array[pritn_val], end=" ")
print(temp_array[pritn_val], end=" ")
print(hum_array[pritn_val], end=" ")
print(loc_array[pritn_val])

pritn_val = 14
print(seed_array[pritn_val], end=" ")
print(soil_array[pritn_val], end=" ")
print(fert_array[pritn_val], end=" ")
print(water_array[pritn_val], end=" ")
print(light_array[pritn_val], end=" ")
print(temp_array[pritn_val], end=" ")
print(hum_array[pritn_val], end=" ")
print(loc_array[pritn_val])

pritn_val = 55
print(seed_array[pritn_val], end=" ")
print(soil_array[pritn_val], end=" ")
print(fert_array[pritn_val], end=" ")
print(water_array[pritn_val], end=" ")
print(light_array[pritn_val], end=" ")
print(temp_array[pritn_val], end=" ")
print(hum_array[pritn_val], end=" ")
print(loc_array[pritn_val])

pritn_val = 13
print(seed_array[pritn_val], end=" ")
print(soil_array[pritn_val], end=" ")
print(fert_array[pritn_val], end=" ")
print(water_array[pritn_val], end=" ")
print(light_array[pritn_val], end=" ")
print(temp_array[pritn_val], end=" ")
print(hum_array[pritn_val], end=" ")
print(loc_array[pritn_val])

# print(seed)
# print(seed_to_soil)
# print(soil_to_fert)
# print(fert_to_water)
# print(water_to_light)
# print(light_to_temp)
# print(temp_to_hum)
# print(hum_to_locat)

