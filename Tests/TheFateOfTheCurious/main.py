import time

class ProblemState:
    def __init__(
        self,
        next_id = 0,
        needed_skills = set(),
        include_set = set()
    ):
        self.next_id = next_id
        self.needed_skills = needed_skills
        self.include_set = include_set

class SearchTimeout(Exception):
    pass


class Solver:

    def __init__(self):
        self.best = None
        self.time = time.time() + 9.9
        self.Load()

    def Load(self):
        # First line has N and K values (candidates and required skills)
        line1 = input().split()
        self.num_candidates = int(line1[0])
        self.num_required_skills = int(line1[1])
        
        # Second line has K specific required skills
        self.required_skills_set = set(input().split())
        
        self.candidates = []
        for _ in range(self.num_candidates):
            num_skills = input()
            if num_skills.isdigit():
                skills = set(input().split())
            else:
                skills = set()
            self.candidates.append((num_skills, skills))
        self.candidates.sort(key=lambda x: len(x[1]), reverse=True)

        delete_list = []
        # i want to prune out the candidates that are subsets of other candidates
        for candidate in reversed(self.candidates):
            for comparing_candidate in self.candidates:
                if candidate != comparing_candidate:
                    if candidate[1].issubset(comparing_candidate[1]):
                        delete_list.append(candidate)
                        break
        for candidate in delete_list:
            if candidate in self.candidates:
                self.num_candidates -= 1
                #print(f"candidate {candidate} is being deleted")
                self.candidates.remove(candidate)
        # sort list by number of skills in descending order
        #print(f"number of candidates: {self.num_candidates}")
        #print(f"candidates: {self.candidates}")
        self.candidates.sort(key=lambda x: len(x[1]), reverse=True)

    def TestValid(self, state: ProblemState) -> bool:
        """
        Tests if the chosen candidates in the current state provide all required skills
        """
        # Since we remove skills as we add candidates, a state is valid if needed_skills is empty!
        return len(state.needed_skills) == 0

    def IncludeCandidate(self, state: ProblemState, candidate_id: int):
        state.include_set.add(candidate_id)
        # Remove the skills this candidate provides from the needed bundle
        state.needed_skills = state.needed_skills.difference(self.candidates[candidate_id][1])

    # Entry point to running the solver
    def Solve(self):
        # Build initial problem state
        initial_state = ProblemState()
        initial_state.needed_skills = set(self.required_skills_set)

        # --- Greedy Initialization ---
        uncovered = set(self.required_skills_set)
        greedy_count = 0
        available_candidates = list(range(self.num_candidates))
        
        while uncovered and available_candidates:
            best_cand = None
            best_intersect = 0
            for c in available_candidates:
                overlap = len(self.candidates[c][1].intersection(uncovered))
                if overlap > best_intersect:
                    best_intersect = overlap
                    best_cand = c
                    
            if best_cand is None:
                break
                
            uncovered.difference_update(self.candidates[best_cand][1])
            available_candidates.remove(best_cand)
            greedy_count += 1
            
        if len(uncovered) == 0:
            self.best = greedy_count
            #   print(f"Greedy algorithm found initial setup of {self.best} candidates. Staring search...")
        else:
            self.best = self.num_candidates + 1
        # -----------------------------

        # Let the branch method handle everything cleanly
        self.Branch(initial_state)
        return self.best

    def Branch(self, state: ProblemState):
        num_candidates_chosen = len(state.include_set)
        
        # Is this a valid solution?
        if len(state.needed_skills) == 0:
            if num_candidates_chosen < self.best:
                self.best = num_candidates_chosen
            return
            
        if num_candidates_chosen >= self.best - 1:
            return
            
        # if we have checked all candidates, return
        if state.next_id >= self.num_candidates:
            return
            
        cur_candidate = state.next_id
        c_skills = self.candidates[cur_candidate][1]
        
        max_possible_skills = len(c_skills) if len(c_skills) > 0 else 1
        # Calculate the absolute minimum number of additional candidates we need simply using divisions
        min_extra_needed = (len(state.needed_skills) + max_possible_skills - 1) // max_possible_skills
        if num_candidates_chosen + min_extra_needed >= self.best:
            return
        
        
        # Check an "Include" branch ONLY if they add something new!
        overlap = c_skills.intersection(state.needed_skills)
        if overlap:
            state.include_set.add(cur_candidate)
            state.needed_skills.difference_update(overlap)
            state.next_id += 1
            
            self.Branch(state)
            

            state.include_set.remove(cur_candidate)
            state.needed_skills.update(overlap)
            state.next_id -= 1
            
        state.next_id += 1
        self.Branch(state)
        state.next_id -= 1


if __name__ == "__main__":
    solver = Solver()
    result = solver.Solve()
    print(result)