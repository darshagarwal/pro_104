from collections import Counter
import csv
from functools import partial

with open("class 104/SOCR-HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_list=list(reader)
file_list.pop(0)

list_data=[]

for i in range(len(file_list)):
    wei=float(file_list[i][2])
    list_data.append(wei)

data=Counter(list_data)

mode_data_for_range= {"75-85":0,
                     "85-95":0,
                     "95-105":0,
                     "105-115":0,
                     "115-125":0,
                     "125-135":0,
                     "135-145":0,
                     "145-155":0,
                     "155-165":0,
                     "165-175":0,
                     }

for weight,occurence in data.items():
    if 75<float(weight)<85:
        mode_data_for_range["75-85"]+=occurence
    elif 85<float(weight)<95:
        mode_data_for_range["85-95"]+=occurence
    elif 95<float(weight)<105:
        mode_data_for_range["95-105"]+=occurence
    elif 105<float(weight)<115:
        mode_data_for_range["105-115"]+=occurence
    elif 115<float(weight)<125:
        mode_data_for_range["115-125"]+=occurence
    elif 125<float(weight)<135:
        mode_data_for_range["125-135"]+=occurence
    elif 135<float(weight)<145:
        mode_data_for_range["135-145"]+=occurence
    elif 145<float(weight)<155:
        mode_data_for_range["145-155"]+=occurence
    elif 155<float(weight)<165:
        mode_data_for_range["155-165"]+=occurence
    elif 165<float(weight)<175:
        mode_data_for_range["165-175"]+=occurence

mode_range,mode_occurence=0,0

for range,occurence in mode_data_for_range.items():
    #print(range.split("-")[1])
    if occurence>mode_occurence:
        mode_range,mode_occurence=[[int(range.split("-")[0]),int(range.split("-")[1])], occurence]

mode=float((mode_range[0]+mode_range[1])/2)

print(f"Mode is -> {mode:2f}")