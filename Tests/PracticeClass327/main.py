skills = {"Athletics", "Acrobatics", "Sleight of Hand", "History", "Nature", "Religion", "Stealth", "Arcana", "Investigation", "Animal Handling", "Insight", "Medicine", "Perception", "Survival", "Deception", "Intimidation", "Performance", "Persuasion"}

class TreeNode:
    def __init__(self, val, solution):
        self.val = val
        self.children = []
        self.solution = solution

class Person:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

class Solution:
    def __init__(self, chosen_people, covered_skills):
        self.chosen_people = chosen_people
        self.covered_skills = covered_skills


bertha = Person("Bertha", {"Investigation", "Stealth", "Sleight of Hand", "Arcana", "Acrobatics", "Intimidation"})
george = Person("George", {"Survival", "Investigation", "Religion", "Animal Handling"})
bannister = Person("Bannister", {"Persuasion", "Survival", "Religion", "Animal Handling"})
agnes = Person("Agnes", {"Perception"})
marian = Person("Marian", {"Performance", "Deception"})
peggy = Person("Peggy", {"Performance", "Survival", "Insight", "Athletics"})
ada = Person("Ada", {"Perception", "Investigation", "Arcana", "Medicine"})
luke = Person("Luke", {"History", "Nature", "Religion"})

solution = Solution([],set())

#people = [bertha, george, bannister, agnes, marian, peggy, ada, luke]

if __name__ == "__main__":
    # we start with luke and check if adding luke is the best solution so far

    # we add luke treenode with the solution
    solution.chosen_people.append(luke.name)
    solution.covered_skills.update(luke.skills)

    print(solution.chosen_people, solution.covered_skills)