class ProblemState:
    def __init__(
        self,
        include_set = set()
    ):
        self.include_set = include_set


class Solver:

    def __init__(self):
        self.num_stars = 0
        self.num_connections = 0
        self.graph = None
        self.best = None
        self.Load()

    def Load(self):
        self.num_stars, self.num_connections = map(int, input().split(" "))
        self.graph = {vertex_id: set() for vertex_id in range(self.num_stars)}
        # TODO: we can optimize by ordering them by number of connections in descending order
        for _ in range(self.num_connections):
            a, b = map(int, input().split(" "))
            # Add edge between a <---> b
            self.graph[a].add(b)
            self.graph[b].add(a)
        self.best = self.num_stars # TODO: optimize here by using a greedy algorithm to find a better than worst case

    def Greedy(self):
        pass

    def TestValid(self, state: ProblemState):
        for system_id in range(self.num_stars):
            # If system has a station, all of its hyper relays have a toll station.
            if system_id in state.include_set:
                continue
            # Otherwise, we need to check that all hyper relays connected to this system have a toll station on the other end.
            for conn_id in self.graph[system_id]:
                if not conn_id in state.include_set:
                    return False
        return True

    def IncludeSystem(self, state: ProblemState, system_id: int):
        state.include_set.add(system_id)

    def RemoveFromSystem(self, state: ProblemState, system_id: int):
        state.include_set.remove(system_id)
        
    # Entry point to running the solver
    def Solve(self):
        # Build initial problem state
        initial_state = ProblemState(set())

        cur_system = 0

        # Try including the current system under consideration
        # TODO: this is where we would pass in the greedy output, we should wrap this in an if statement
        # if the count is equal to or greater than self.best, we can stop
        # we don't need to check if its a valid solution because we already know a better one exists
        self.IncludeSystem(initial_state, cur_system)
        self.Branch(initial_state, cur_system + 1)
        self.RemoveFromSystem(initial_state, cur_system)
        
        # Try excluding the current system under consideration
        self.Branch(initial_state, cur_system + 1)

        return self.best

    def Branch(self, state: ProblemState, current_id: int):
        # Current count of systems with stations
        num_stations = len(state.include_set)
        # Is this a valid solution?
        valid_sol = self.TestValid(state)
        # If so, if better than best, update best and bail out of this branch.
        if (valid_sol and num_stations < self.best):
            self.best = num_stations
            return
        # Not a solution. If next_id is not valid, return.
        if (current_id >= self.num_stars):
            return
        # If we're here, next_id is valid and we don't yet have a solution on this branch.
        cur_system = current_id

        # Try including the current system under consideration
        self.IncludeSystem(state, cur_system)
        self.Branch(state, cur_system + 1)
        self.RemoveFromSystem(state, cur_system)

        # Try excluding the current system under consideration
        self.Branch(state, cur_system + 1)


if __name__ == "__main__":
    solver = Solver()
    result = solver.Solve()
    print(result)



"""
RESULTS:
un-optimized:
jojo@jojo-mac final % time python3 main.py < test_3_random.txt
11
python3 main.py < test_3_random.txt  19.24s user 0.07s system 99% cpu 19.326 total

backtracking optimization:
jojo@jojo-mac final % time python3 main.py < test_3_random.txt
11
python3 main.py < test_3_random.txt  2.38s user 0.02s system 99% cpu 2.410 total

greedy pre-process optimization:

NOTES:
Starting off by thinkning about optimizing how we define worst case, we could do a greedy to find a better than worst case and start there to weed out
My first optimization attempt is by using backtracking instead of doing a copy each time. I removed next_id from the class
and I just pass current_id into branch, this way I dont need to book keep the id 


"""