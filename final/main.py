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
        for _ in range(self.num_connections):
            a, b = map(int, input().split(" "))
            # Add edge between a <---> b
            self.graph[a].add(b)
            self.graph[b].add(a)

        self.ordered_vertices = sorted(
            self.graph.keys(), 
            key=lambda vertex_id: len(self.graph[vertex_id]), 
            reverse=True
        )
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
        self.Branch(initial_state, 0)
        return self.best


    def Branch(self, state: ProblemState, current_id: int):
        # Current count of systems with stations
        num_stations = len(state.include_set)
        # if the current number of stations is already larger than or equal to best - 1 there is no need to search as we 
        # will not find a better solution
        if num_stations >= self.best - 1:
            return

        valid_sol = self.TestValid(state)
        # If so, if better than best, update best and bail out of this branch.
        if (valid_sol and num_stations < self.best):
            # print(f"num stations {num_stations}")
            self.best = num_stations
            return
        # Not a solution. If next_id is not valid, return.
        if (current_id >= self.num_stars):
            return
        # If we're here, next_id is valid and we don't yet have a solution on this branch.
        cur_system = self.ordered_vertices[current_id]

        self.IncludeSystem(state, cur_system)
        self.Branch(state, current_id + 1)
        self.RemoveFromSystem(state, cur_system)

        # Try excluding the current system under consideration
        self.Branch(state, current_id + 1)


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

bounding optimizations:
jojo@jojo-mac final % time python3 main.py < test_3_random.txt
11
python3 main.py < test_3_random.txt  0.88s user 0.02s system 98% cpu 0.912 total

NOTES:
Starting off by thinkning about optimizing how we define worst case, we could do a greedy to find a better than worst case and start there to weed out
My first optimization attempt is by using backtracking instead of doing a copy each time. I removed next_id from the class
and I just pass current_id into branch, this way I dont need to book keep the id 


"""