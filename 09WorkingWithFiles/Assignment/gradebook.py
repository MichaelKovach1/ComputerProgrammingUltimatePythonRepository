import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 

A_count = 0
B_count = 0
C_count = 0
D_count = 0
F_count = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    if percent <= 60:
        F_count = F_count + 1
    elif percent <= 70:
        D_count = D_count + 1
    elif percent <= 80:
        C_count = C_count + 1
    elif percent <= 90:
        B_count = B_count + 1
    elif percent <= 100:
        A_count = A_count + 1
print("The Number of Each Grade from A-F is:", A_count, B_count, C_count, D_count, F_count)

f.close()

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 

total_f = 0
f_count = 0
total_s = 0
s_count = 0
total_j = 0
j_count = 0
total_sr = 0
sr_count = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(gradelevel)
    if gradelevel == 9:
        total_f = total_f + percent
        f_count = f_count + 1
    elif gradelevel == 10:
        total_s = total_s + percent
        s_count = s_count + 1
    elif gradelevel == 11:
        total_j = total_j + percent
        j_count = j_count + 1
    elif gradelevel == 12:
        total_sr = total_sr + percent
        sr_count = sr_count + 1
avgf = total_f/f_count
avgs = total_s/s_count
avgj = total_j/j_count
avgsr = total_sr/sr_count
print("The Average Grades of all the Classes From Freshman-Seniors is:", avgf, avgs, avgj, avgsr)

f.close()

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
namelist = []
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(gradelevel)
    if gradelevel == 12 and percent <= 60:
        namelist.append(name)

print("The Names of the Failing Seniors are:", namelist)