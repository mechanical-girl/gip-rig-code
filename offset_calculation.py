import statistics
import csv
from math import sin

base_deflection_offset = 28*sin(30)

with open("output.txt", "r") as f:
    filelines = f.read().split("\n")

input_data = {}
for line in filelines:
    angle, force = line.split(",")

    if angle not in input_data.keys(): # This is the first time this has angle has been encountered
        input_data[angle] = [float(force)]
    else: # The array exists and we can append to it
        input_data[angle].append(float(force))

# In preparation for writing this out in CSV format, we're putting all the data in a list of lists
# List order is as follows:
# Angle,Calculated Deflection,Force 1,Force 2,Force 3,Mean Force,Std Dev
processed_data=[]
for key in input_data.keys():
    angle = int(key)
    this_dataset = [angle]
    this_dataset.append((28*sin(30+angle))-base_deflection_offset) # Calculate the deflection at this angle

    this_dataset += input_data[key]

    this_dataset.append(sum(input_data[key])/3)
    this_dataset.append(statistics.stdev(input_data[key]))
    processed_data.append(this_dataset)

with open("data.csv", 'w', newline='') as outputfile:
    writer = csv.writer(outputfile)
    for dataset in processed_data:
        writer.writerow(dataset)
