import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def polar_to_cartesian(angle_degrees, distance_mm):
    angle_radians = np.deg2rad(angle_degrees)
    x = distance_mm * np.cos(angle_radians)
    y = distance_mm * np.sin(angle_radians)
    z = 0  # assuming z coordinate is 0 (sensor at height 0)
    return x, y, z

def plot_3d_scatter(coordinates):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = coordinates[:, 0]
    y = coordinates[:, 1]
    z = coordinates[:, 2]

    ax.scatter(x, y, z, c=z, cmap='viridis', s=10)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Scans Data in 3D Cartesian Coordinates')

    plt.show()

def process_scans_data(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    coordinates = []
    for timestamp in data:
        for scan_data in data[timestamp]:
            angle = scan_data[2]  # Assuming angle is stored at index 2 in each scan_data list
            distance = scan_data[0]  # Assuming distance is stored at index 0 in each scan_data list
            intensity = scan_data[1]  # Assuming intensity is stored at index 1 in each scan_data list
            
            x, y, z = polar_to_cartesian(angle, distance)
            coordinates.append([x, y, z])
    
    coordinates = np.array(coordinates)
    return coordinates

# Input and output file names
input_file = "scans_data_with_angles.json"

# Process scans data to get Cartesian coordinates
coordinates = process_scans_data(input_file)

# Plot the points in 3D
plot_3d_scatter(coordinates)
