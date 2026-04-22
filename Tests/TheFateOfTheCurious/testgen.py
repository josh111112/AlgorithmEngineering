import random
import sys

N = int(sys.argv[1])
K = 20

skills = [f"Skill{i}" for i in range(1, K+1)]

with open("test_input.txt", "w") as f:
    f.write(f"{N} {K}\n")
    f.write(" ".join(skills) + "\n")
    
    for i in range(N):
        # Pick a random number of skills (between 1 and a portion of K)
        num_c_skills = random.randint(1, min(4, K))
        c_skills = random.sample(skills, num_c_skills)
        f.write(f"{len(c_skills)}\n")
        f.write(" ".join(c_skills) + "\n")
