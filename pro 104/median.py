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
list_data.sort()

if num%2==0:
    median1=float(list_data[num//2])
    median2=median1=float(list_data[num//2-1])
    median=(median1+median2)/2
else:
    median=float(list_data[num//2])

print(median)