MOD = 1000000009

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        cache = {}
        num_blocks, max_length = map(int, input().split())
        block_sizes = list(map(int, input().split()))
        print(grow(max_length, block_sizes, cache))
def grow(remaining, block_sizes, cache):
    if remaining in cache:
        return cache[remaining]
    
    count = 0
    for block in block_sizes:
        new_remaining = remaining - block
        if new_remaining > 0:
            count += grow(new_remaining, block_sizes, cache)
        elif new_remaining == 0:
            count += 1
    
    cache[remaining] = count % MOD
    return cache[remaining]

    return count % 1000000009
if __name__ == "__main__":
    main()