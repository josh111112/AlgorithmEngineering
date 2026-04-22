if __name__ == "__main__":
    num_contestants = int(input())
    numbers = list(map(int, input().split()))
    contestants_alive = num_contestants
    start_idx = min(numbers) 
    prev_num_contestants = contestants_alive
    print(contestants_alive)
    while contestants_alive > 1:
        numbers = [x for x in numbers if x != start_idx]
        contestants_alive = len(numbers)
        if prev_num_contestants != contestants_alive and contestants_alive != 0:
            print(contestants_alive)
        prev_num_contestants = contestants_alive
        start_idx += 1