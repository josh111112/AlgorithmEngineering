import bisect

def main():
    num_inputs = int(input())
    median_list = []
    median = 0
    median_idx = 0
    for _ in range(num_inputs):
        operation, num = input().split()
        num = int(num)
        if operation == 'r':
            if not median_list or num not in median_list:
                print("Wrong!")
                continue
            median_list.remove(num)
        else:
            bisect.insort(median_list, num)

        if len(median_list) % 2 == 1:
            median_idx = int((len(median_list) // 2) // 1) # ceiling division
            print(f"{median_list[median_idx]:g}")
        else:
            median_idx = (len(median_list) // 2) - 1
            if not median_list:
                print("Wrong!")
                continue
            median = (median_list[median_idx] + median_list[median_idx + 1]) / 2
            print(f"{median:g}")
if __name__ == "__main__":
    main()