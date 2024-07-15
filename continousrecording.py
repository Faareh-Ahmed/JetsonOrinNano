# This code attempts to take continous scans of the sensor
# it creates a generator and takes the infinite scans until specified to stop
# also the data obtained from the 500 scans initially is saved in "scans_data.json" which contains
# data of 6.7MB of just 500 scans. It records both range + intensity 

import json
import numpy as np
from hokuyolx import HokuyoLX
laser = HokuyoLX()

print(laser.version())
# Checking the scanner state
print("\nState of the Scanner:")
print(laser.laser_state())

scan_generator=laser.iter_intens(scans=0)

print(type(scan_generator))

# Dictionary to store the collected scans
scans_data = {}
print(type(next(scan_generator)))
# print(next(scan_generator))

# timestamp, scan_dataed, typed = next(scan_generator)
# print(timestamp)
# print(scan_dataed)
# print(typed)
try:
    # Taking 500 scans
    for i in range(500):
        scan_data,timestamp,typed  = next(scan_generator)
        scans_data[timestamp] = scan_data.tolist()
        print(f"Scan {i+1}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Write collected data to a text file
    file_name = "scans_data.json"
    with open(file_name, 'w') as f:
        json.dump(scans_data, f, indent=None)  # Save dictionary as JSON with indentation for readability
    print(f"Data saved to {file_name}")


    