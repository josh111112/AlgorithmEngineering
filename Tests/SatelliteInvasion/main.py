def picker():
    num_satellites = int(input())

    cost = 0
    starting_satellite = 0
    for satellite_node in range(num_satellites):
        energy_available, cost_to_next_satellite = input().split()
        energy_available = int(energy_available)
        cost_to_next_satellite = int(cost_to_next_satellite)
        if cost < 0:
            #print("chainging starting sat", satellite_node)
            starting_satellite = satellite_node
            cost = 0
        #print("starting cost", cost)
        cost += energy_available
        #print("cost after energy gained", cost)
        cost -= cost_to_next_satellite
        #print("cost after travling to next sat", cost)


    #print(satellite_list)
    # we want to pick a satellite where when we loop through the list, we keep track of the energy given and the energy taken
    # energy taken must never go below 0

    # start at the beginning and if the energy reaches below 0 go to the current node and choose that as your next starting node
    #print(starting_satellite)
    print(starting_satellite)
if __name__ == "__main__":
    picker()