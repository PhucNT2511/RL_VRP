from sklearn.preprocessing import MinMaxScaler
import math
import numpy as np

def read_input_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    truck_capacity = int(lines[2].split(':')[1].strip())
    num_customers = int(lines[1].split(':')[1].strip())

    location_index = lines.index("LOCATION\n") + 1
    demand_index = lines.index("DEMAND_SECTION\n") + 1

    locations = []
    demands = []
    for i in range(location_index, demand_index - 1):
        parts = lines[i].split()
        locations.append([float(parts[1]), float(parts[2])])

    for i in range(demand_index, len(lines) - 1):
        if "DEPOT_SECTION" in lines[i] or "EOF" in lines[i]:
            break
        parts = lines[i].split()
        demands.append(int(parts[1]))

    max_demand = max(demands)
    max_load = truck_capacity

    # Scale coordinates
    scaler = MinMaxScaler()
    locations_scaled = scaler.fit_transform(locations)

    # Normalize demands
    # demands = [demand / float(max_load) for demand in demands]

    return num_customers, max_load, max_demand, locations_scaled, demands

def create_matric():
    num_customers, max_load, max_demand, locations_scaled, demands = read_input_file('C:/Users/DELL/Downloads/txt/input_10_56.txt')
    matrix = []
    for i in range(10):
        row=[]
        for j in range (10):
            row.append(math.sqrt(pow((locations_scaled[i][0]-locations_scaled[j][0]),2)+pow((locations_scaled[i][1]-locations_scaled[j][1]),2)))
        matrix.append(row)
    matrix = np.array(matrix) * 1000
    return matrix, demands, max_load
    