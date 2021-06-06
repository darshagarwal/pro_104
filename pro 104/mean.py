import csv

with open("class 104/SOCR-HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_list=list(reader)
file_list.pop(0)

list_data=[]

for i in range(len(file_list)):
    hei=float(file_list[i][2])
    list_data.append(hei)

num=len(list_data)
total=0

for x in list_data:
    total+=x

mean=total/num

print(mean)