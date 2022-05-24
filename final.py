import csv

from sklearn import datasets

datasets_1=[]
datasets_2=[]

with open("dwarf_stars.csv","r")as f :
    csvreader=csv.reader(f)

    for row in csvreader:
        datasets_1.append(row)


with open("dwarf_stars_sorted1.csv","r")as f :
    csvreader=csv.reader(f)

    for row in csvreader:
        datasets_2.append(row)

header1=datasets_1[0]
star_data1=datasets_1[1:]

header2=datasets_2[0]
star_data2=datasets_2[1:]

header=header1+header2

star_data=[]

for index,row in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])


with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(star_data)