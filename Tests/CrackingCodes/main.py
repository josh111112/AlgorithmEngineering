import heapq

def main():
    def helper(node):
        return (node[1], node[0])
    num_tests = int(input())
    time_spent = 0
    current_time = 0
    all_messages = []
    available = []
    for i in range(num_tests):
        arrival, time_to_decrypt = input().split()
        node = (int(arrival), int(time_to_decrypt))
        heapq.heappush(all_messages, node)
    
    while all_messages or available:
        if len(available) == 0:
            next = heapq.heappop(all_messages)
            available_node = helper(next)
            heapq.heappush(available, available_node)
            current_time = max(current_time, available_node[1])
        while all_messages and current_time >= all_messages[0][0]:
            next = heapq.heappop(all_messages)
            available_node = helper(next)
            heapq.heappush(available, available_node)
        current_job = heapq.heappop(available)
        current_time += current_job[0]
        time_spent += current_time - current_job[1]
    print(time_spent//num_tests)
        
if __name__ == "__main__":
    main()