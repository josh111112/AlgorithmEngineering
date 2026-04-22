

def generate_mapping(s: int, p: int):
    '''
    Return a dictionary mapping of which pies you test with each poison test stick.
    Test sticks are labeled: stick-0, stick-1, stick-2, stick-3, ..., stick-s
    Pies are labeled 0 : 999

    For this problem, s will always = 10, and p will always = 1000
    '''
    # This example return is correctly formatted but will not ensure that you
    # identify the poisoned pie.
    # E.g., in this example, you use stick-0 to test pies 0 and 10.
    dicty = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }
    for i in range(p):
        binstring = bin(i)[2:][::-1]
        
        for bit_index, bit_value in enumerate(binstring):
            if bit_value == '1':
                dicty[f"{bit_index}"].append(i)

    return dicty

def solve(positive_tests: list, test_mapping: dict):
    binstring = ["0"] * 10
    for i in positive_tests:
        index = int(i)

        binstring[index] = "1"

    final = "".join(binstring)[::-1]
    return int(final, 2)