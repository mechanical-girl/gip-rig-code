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

# Data gets organised into a list of dicts
col_names = ["angle", "deflection", "measure 1", "measure 2", "measure 3", "mean", "stddev"]
processed_data=[]
for key in input_data.keys():
    angle = int(key)
    this_dataset = {}
    this_dataset[col_names[0]] = angle

    this_dataset[col_names[1]] = float(28*sin(30+angle))-base_deflection_offset # Calculate the deflection at this angle

    this_dataset[col_names[2]],this_dataset[col_names[3]],this_dataset["measure 3"] = input_data[key]

    this_dataset["mean"] = sum(input_data[key])/3
    this_dataset["stddev"] = statistics.stdev(input_data[key])

    processed_data.append(this_dataset)

with open("data.csv", 'w', newline='') as outputfile:
    writer = csv.DictWriter(outputfile, fieldnames=col_names)
    writer.writeheader()
    for dataset in processed_data:
        writer.writerow(dataset)
