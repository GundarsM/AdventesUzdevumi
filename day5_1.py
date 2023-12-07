import re


file = open("input_day5_t.txt")
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
soil_list = []
seed_list = []
fert_list = []
new_max = 0
for i in range(len(seed_to_soil)):
    test = (seed_to_soil[i][1]+seed_to_soil[i][2]-1)
    if test > new_max: new_max = test

#print(new_max)

for i in range(new_max+1):
    seed_list.append(i)
    soil_list.append(i)
    fert_list.append(i)

# print(len(seed_list))
# print(len(soil_list))

for i in range(len(seed_to_soil)):
    for j in range(seed_to_soil[i][2]):
        soil_list[seed_to_soil[i][1]+j] = seed_to_soil[i][0]+j


#print(soil_list)
counteris = 0


fert_list = soil_list[:]

for i in range(len(soil_to_fert)):              # 3x
    #print(soil_to_fert[i])   
    counteris = 0 
    for k in range(len(seed_list)):             # 100x          
        if soil_list[k] == soil_to_fert[i][1]+counteris:  # ja ir 15
            fert_list[k] = soil_to_fert[i][0]+counteris   # tad fert 15 = 0
            #print(k, fert_list[k], counteris, soil_to_fert[i][0]+counteris)
            counteris += 1            
            if counteris>soil_to_fert[i][2]-1: break            

print(fert_list)

water_list = []

water_list = fert_list[:]
print (water_list)

counteris = 0
for i in range(len(fert_to_water)):              # 3x
    print(fert_to_water[i])   
    counteris = 0 
    for k in range(len(seed_list)):             # 100x          
        if fert_list[k] == fert_to_water[i][1]+counteris:  # ja ir 49
            water_list[k] = fert_to_water[i][0]+counteris   # tad fert 15 = 0
            print(k, water_list[k], counteris, fert_to_water[i][0]+counteris)
            counteris += 1            
            if counteris>fert_to_water[i][2]-1: break            

print(water_list)

pritn_val = 79
print(seed_list[pritn_val], end=" ")
print(soil_list[pritn_val], end=" ")
print(fert_list[pritn_val], end=" ")
print(water_list[pritn_val])

pritn_val = 14
print(seed_list[pritn_val], end=" ")
print(soil_list[pritn_val], end=" ")
print(fert_list[pritn_val], end=" ")
print(water_list[pritn_val])

pritn_val = 55
print(seed_list[pritn_val], end=" ")
print(soil_list[pritn_val], end=" ")
print(fert_list[pritn_val], end=" ")
print(water_list[pritn_val])

pritn_val = 13
print(seed_list[pritn_val], end=" ")
print(soil_list[pritn_val], end=" ")
print(fert_list[pritn_val], end=" ")
print(water_list[pritn_val])


# print(seed)
# print(seed_to_soil)
# print(soil_to_fert)
# print(fert_to_water)
# print(water_to_light)
# print(light_to_temp)
# print(temp_to_hum)
# print(hum_to_locat)

