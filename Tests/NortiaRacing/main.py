if __name__ == "__main__":
    num_tests = int(input())


    for test_idx in range(num_tests):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        n = int(line[2])
        possible_distances = set()
        for i in range(n + 1):
                presses_of_x = i
                presses_of_y = n - i
                distance = (presses_of_x * x) + (presses_of_y * y)
                possible_distances.add(distance)
        print(*sorted(list(possible_distances)))