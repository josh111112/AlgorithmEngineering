def solve(num_brick_types, max_power, brick_speeds):
    found = False
    smallest_brick = min(brick_speeds)

    def initialize(brick_types, max_power):
        return [max_power - brick for brick in brick_types if max_power - brick >= 0]

    if not found:
        bricks_still_fit = True
        dp = initialize(brick_speeds, max_power)
        while bricks_still_fit:
            for brick_index, brick in enumerate(brick_speeds):
                ctr = 0
                temp_list = []
                for value in range(len(dp)):
                    if dp[value] % brick == 0:
                        return max_power - dp[value] % brick
                    if dp[value] > brick:
                        temp = dp[value] - brick
                        if temp == 0:
                            return max_power - temp
                        elif temp > 0:
                            ctr += 1
                            dp.append(temp)
                            temp_list.append(dp[value])
            for num in temp_list:
                dp.remove(num)
            temp_list = []
            if ctr == 0 and brick_index == num_brick_types - 1:
                bricks_still_fit = False
        if not found and len(dp) > 0:
            return max_power - min(dp)
        else:
            return 0


def main():
    num_tests = int(input())
    for case_index in range(num_tests):
        num_brick_types, max_power = map(int, input().split())
        brick_speeds = list(map(int, input().split()))
        result = solve(num_brick_types, max_power, brick_speeds)
        print(result)


if __name__ == "__main__":
    main()



    """
    first run: 
    python3 main.py < big_test.txt  23.80s user 0.33s system 99% cpu 24.145 total

    second run: 
    python3 main.py < big_test.txt  24.85s user 0.36s system 99% cpu 25.330 total
    
    third run:
    python3 main.py < big_test.txt  24.02s user 0.36s system 99% cpu 24.401 total   
    
    fourth run:
    python3 main.py < big_test.txt  12.57s user 0.13s system 99% cpu 12.718 total
    """