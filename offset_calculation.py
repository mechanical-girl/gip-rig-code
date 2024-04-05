with open("output.txt", "r") as f:
    filelines = f.read().split("\n")

processed_data = {}
for line in filelines:
    angle, force = line.split(",")

    if angle not in processed_data.keys(): # This is the first time this has angle has been encountered
        processed_data[angle] = [force]
    else: # The array exists and we can append to it
        processed_data[angle].append(force)

