if __name__ == "__main__":
    num_tests = int(input())


    for test_idx in range(num_tests):
            line = input().split()
            n = int(line[0]) # gallons of fuel.  6
            m = int(line[1]) # number of gallons per cell. 2. 3 fuel cells
            c = int(line[2]) # number of used cells to make new cell. 2
            full_cells = n//m
            distance_traveled = 0
            num_empty_cells = 0
            while full_cells > 0:
                distance_traveled += full_cells # 3
                num_empty_cells += full_cells # 3
                full_cells = num_empty_cells // c # (3 // 2 = 1) 
                num_empty_cells = num_empty_cells - (c * (num_empty_cells // c)) # 3 - (2 * 1)
            print(distance_traveled)