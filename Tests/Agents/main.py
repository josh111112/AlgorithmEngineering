def main():
    # Read n and m from the first line
    try:
        # map converts the space-separated strings to integers
        n, m = map(int, input().split())
        
        # create a list of tuples with their index and a counter
        agents = [(i, 1) for i in range(1, m + 1)]
        # Read the second line of n space-separated positive integers
        c = list(map(int, input().split()))        
    except (EOFError, ValueError) as e:
        print(f"Error reading input: {e}")



    c.sort(reverse=True)
    sum = 0
    # loop through list, and give each agent the highest number
    for i in range(n):
        # the agent with the lowest counter gets the highest number
        agents.sort(key=lambda x: x[1])
        # we want to grab the first agent and add the number to the sum
        current_counter = agents[0][1]
        sum = sum + (c[i] * current_counter)
        agent_id = agents[0][0]
        agents[0] = (agent_id, current_counter + 1)
    
    print(sum)
if __name__ == "__main__":
    main()
