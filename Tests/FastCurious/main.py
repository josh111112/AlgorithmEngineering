def main():
    num_bricks = int(input())
    brick_list = list(map(int, input().split()))
    dp = [0] * num_bricks
    def solve(index):
        if index == 0:
            dp[index] = brick_list[index]
            return
        if index == 1:
            dp[index] = max(brick_list[0], brick_list[1])
            return
        dp[index] = max(dp[index-1], dp[index-2]+brick_list[index])
    
    for index in range(num_bricks):
        solve(index)
    
    print(dp[num_bricks-1])


if __name__ == "__main__":
    main()