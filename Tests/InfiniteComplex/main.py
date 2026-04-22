if __name__ == "__main__":
    num_tests = int(input())


    for test_idx in range(num_tests):
        x = int(input())
        print(f'{(8 * ((x * (x+1))//2))+ (x != 1)}')