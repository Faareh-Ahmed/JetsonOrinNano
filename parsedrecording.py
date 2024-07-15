import json

def parse_and_append_angles(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    for timestamp in data:
        angle = 0.0
        for scan_data in data[timestamp]:
            scan_data.append(angle)
            angle += 0.25
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=None)  # Save dictionary as JSON without indentation for compactness

    print(f"Appended data saved to {output_file}")

# Input and output file names
input_file = "scans_data.json"
output_file = "scans_data_with_angles.json"

# Call the function to parse and append angles
parse_and_append_angles(input_file, output_file)