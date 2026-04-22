import math

if __name__ == "__main__":
    num_tests = int(input())


    for test_idx in range(num_tests):
            line = input().split()
            n = int(line[0]) # lower bound
            m = int(line[1]) # upper bound
            d = (m // 12) - ((n - 1) // 12)
            upper_root = int(math.isqrt(m))
            lower_root = int(math.isqrt(n - 1))     
            s = upper_root - lower_root
            b = 0

            k = 1
            while True:
                val = 36 * (k**2)
                if val > m:
                    break
                if val >= n:
                    b += 1
                k += 1

            print(f'{d} {s} {b}')
