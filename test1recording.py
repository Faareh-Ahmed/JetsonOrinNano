# this is the code that takes the single scan of the sensor
# and also takes continous scans based on the iteration definSed
# It outputs the Distance ranges of the Scans

from hokuyolx import HokuyoLX
laser = HokuyoLX()
print(laser.version())
# Checking the scanner state
print("State of the Scanner:\n")
print(laser.laser_state())

# Single measurment mode
print("Single Measurement Mode:\n")
scan = laser.get_dist(start=90,end=180,grouping=1) 
print(type(scan))
print(scan)

# Continous measurment mode
print("Continous Measurement Mode:\n")
for idx, scan in enumerate(laser.iter_dist(1)):
    distances = []
    for distance in scan[0]:
        distances.append(distance)
    
    # Print all distances for the current scan
    print(f"Scan {idx}: measurements: {len(distances)}\n {distances}\n Max Range is {max(distances)}\n")







