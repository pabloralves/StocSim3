"""
Plots the datasets in the txt files to include them in the report
and perhaps in the results for comparisson reasons.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Read the file (same code from notebook)
# 1.1 Locations
def load_tsp_file(file_path):
    """ Loads the (x,y) coordinates for the TSP problem from a txt
    as a dictionary """

    tsp_data = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Flag to indicate the start of the NODE_COORD_SECTION
    start_loading = False

    for line in lines:
        # Strip leading and trailing whitespaces
        line = line.strip()

        # Check for the start of the NODE_COORD_SECTION
        if line == "NODE_COORD_SECTION":
            start_loading = True
            continue

        # Check for the end of the file
        if line == "EOF":
            break

        if start_loading:
            parts = line.split()
            
            # Extract node number, x-coordinate, and y-coordinate
            node_number = int(parts[0])
            x_coordinate = float(parts[1])
            y_coordinate = float(parts[2])

            # Store data in the dictionary
            tsp_data[node_number] = np.array([x_coordinate, y_coordinate])

    # Check if the dataset is as intuitive as it appears
    nodes = set(tsp_data.keys())
    highest_number = max(nodes)
    missing_nodes = set(range(1, highest_number + 1)) - nodes

    if missing_nodes:
        print(f"Note that not all numbers between 0 and {highest_number} are used as a node ID. Node(s) {missing_nodes} are missing.")

    return tsp_data

# 1.2 Best route
def load_optimal_tsp_file(file_path):
    """ Loads the best route for the TSP problem
    and returns it as a np array"""
    
    tsp_data = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Flag to indicate the start of the TOUR_SECTION
    start_loading = False

    for line in lines:
        # Strip leading and trailing whitespaces
        line = line.strip()

        # Check for the start of the TOUR_SECTION
        if line == "TOUR_SECTION":
            start_loading = True
            continue

        # Check for the end of the file
        # NEW! We now end at -1 to avoid adding extra elements to the route
        if line == "-1":
            break

        if start_loading:
            tsp_data.append(int(line))

    return np.array(tsp_data)


# Read the actual files
tsp_data = load_tsp_file("./TSP-Configurations/eil51.tsp.txt")

def get_score(tsp_data, solution):
    """ Computes the associated score of a TSP solution
    using standard 2D Euclidean distance """
    distance = 0
    coordinates = solution[0]
    for city in solution[1:]:
        next_coordinates = tsp_data[city]
        distance += np.linalg.norm(coordinates - next_coordinates)
        coordinates = next_coordinates.copy()

    return distance

"""
# Load data for 51 location TSP
file = 'eil51'
file = 'a280'
file = 'pcb442'
file_path = f'TSP-Configurations/{file}.tsp.txt'
tsp_data = load_tsp_file(file_path)

# Also load optimal solution
file_path = f'TSP-Configurations/{file}.opt.tour.txt'
optimal_tsp_route = load_optimal_tsp_file(file_path)

# 2. Plot
# 2.1 Locations
for point in tsp_data.values():
    plt.scatter(point[0],point[1],color='black')

#plt.show()
# 2.2 Route



current_node = optimal_tsp_route[0]
for next in optimal_tsp_route:

    # Get extremes of connection
    next_node = next

    # Get coordinates of those nodes
    origin  = tsp_data.get(current_node)
    destiny = tsp_data.get(next_node)

    # Plot line with arrow :)
    plt.plot([origin[0],destiny[0]],[origin[1],destiny[1]],'--',color='blue')
    
    # Update node
    current_node = next_node

# Add last trip returning home
origin  = tsp_data.get(optimal_tsp_route[-1])
destiny = tsp_data.get(optimal_tsp_route[0])
plt.plot([origin[0],destiny[0]],[origin[1],destiny[1]],'--',color='red')

plt.legend()
plt.show()
"""

# Do 3 plots together
## Read data from three files

## Plots...
tsp_data_1 = load_tsp_file('TSP-Configurations/eil51.tsp.txt')
tsp_data_2 = load_tsp_file('TSP-Configurations/a280.tsp.txt')
tsp_data_3 = load_tsp_file('TSP-Configurations/pcb442.tsp.txt')

optimal_tsp_route_1 = load_optimal_tsp_file('TSP-Configurations/eil51.opt.tour.txt')
optimal_tsp_route_2 = load_optimal_tsp_file('TSP-Configurations/a280.opt.tour.txt')
optimal_tsp_route_3 = load_optimal_tsp_file('TSP-Configurations/pcb442.opt.tour.txt')


fig, ax = plt.subplots(1,3,figsize=(7,3),dpi=500)
# Note that ax is now an array consisting of the individual axis

#print(tsp_data_1)

#startpoint = tsp_data_1.get('1')
#print(startpoint)
#ax[0].scatter(startpoint[0],startpoint[1],color='red')

# Add grid
ax[0].set_axisbelow(True)
ax[1].set_axisbelow(True)
ax[2].set_axisbelow(True)
ax[0].grid()
ax[1].grid()
ax[2].grid()


# Plot points
for point in tsp_data_1.values():
    ax[0].scatter(point[0],point[1],color='tab:blue',s=6)

for point in tsp_data_2.values():
    ax[1].scatter(point[0],point[1],color='tab:orange',s=6)

for point in tsp_data_3.values():
    ax[2].scatter(point[0],point[1],color='tab:green',s=6)

# Plot route
# CITY 1
current_node = optimal_tsp_route_1[0]
for next in optimal_tsp_route_1:
    # Get extremes of connection and coordinates of those nodes    
    next_node = next
    origin  = tsp_data_1.get(current_node)
    destiny = tsp_data_1.get(next_node)
    # Plot line and update node
    ax[0].plot([origin[0],destiny[0]],[origin[1],destiny[1]],linestyle=(0, (1, 1)),color='tab:blue',linewidth=1)  
    current_node = next_node

# Add last trip returning home and origin point
origin  = tsp_data_1.get(optimal_tsp_route_1[-1])
destiny = tsp_data_1.get(optimal_tsp_route_1[0])
ax[0].plot([origin[0],destiny[0]],[origin[1],destiny[1]],linestyle=(0, (1, 1)),color='tab:blue',linewidth=1) 
ax[0].scatter(origin[0],origin[1],color='red',s=12)

# CITY 2
current_node = optimal_tsp_route_2[0]
for next in optimal_tsp_route_2:
    # Get extremes of connection and coordinates of those nodes    
    next_node = next
    origin  = tsp_data_2.get(current_node)
    destiny = tsp_data_2.get(next_node)
    # Plot line and update node
    ax[1].plot([origin[0],destiny[0]],[origin[1],destiny[1]],linestyle=(0, (1, 1)),color='tab:orange',linewidth=1)  
    current_node = next_node

# Add last trip returning home and origin point
origin  = tsp_data_2.get(optimal_tsp_route_2[-1])
destiny = tsp_data_2.get(optimal_tsp_route_2[0])
ax[1].plot([origin[0],destiny[0]],[origin[1],destiny[1]],linestyle=(0, (1, 1)),color='tab:orange',linewidth=1) 
ax[1].scatter(origin[0],origin[1],color='red',s=12)

# CITY 3
current_node = optimal_tsp_route_3[0]
for next in optimal_tsp_route_3:
    # Get extremes of connection and coordinates of those nodes    
    next_node = next
    origin  = tsp_data_3.get(current_node)
    destiny = tsp_data_3.get(next_node)
    # Plot line and update node
    ax[2].plot([origin[0],destiny[0]],[origin[1],destiny[1]],linestyle=(0, (1, 1)),color='tab:green',linewidth=1)  
    current_node = next_node

# Add last trip returning home and origin point
origin  = tsp_data_3.get(optimal_tsp_route_3[-1])
destiny = tsp_data_3.get(optimal_tsp_route_3[0])
ax[2].plot([origin[0],destiny[0]],[origin[1],destiny[1]],linestyle=(0, (1, 1)),color='tab:green',linewidth=1) 
ax[2].scatter(origin[0],origin[1],color='red',s=12)





# Make xlim and ylim start at 0
ax[0].set_xlim([0,ax[0].get_xlim()[1]])
ax[1].set_xlim([0,ax[1].get_xlim()[1]])
ax[2].set_xlim([0,ax[2].get_xlim()[1]])

ax[0].set_ylim([0,ax[0].get_ylim()[1]])
ax[1].set_ylim([0,ax[1].get_ylim()[1]])
ax[2].set_ylim([0,ax[2].get_ylim()[1]])

# Put title
#ax[0].set_title('51')
#ax[1].set_title('280')
#ax[2].set_title('442')



# Show
plt.tight_layout()
plt.savefig('cities.png')
print('Done!')