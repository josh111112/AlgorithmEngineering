def prepare(names, num_scratches):
    '''
    Called once before any games are played.
    Each person during each game receives a copy of this for their scratch decisions.

    names: list of names of people playing the game
    num_scratches: maximum number of scratches allowed per person when playing
    '''
    sorted_names = sorted(names)
    dicty = {}
    for i in range(len(names)):
        dicty[sorted_names[i]] = i
    return dicty


def scratch(
    name: str,
    ticket_state: list,
    revealed_names: dict,
    scratch_history: list,
    prepared_info = None
):
    '''
    Each person in names (from prepare) will be allowed to scratch up to num_scratches (from prepare)
    number of positions on their lottery ticket. This function is how you write implement the strategy you
    want each person to follow.

    Parameters:
    - name (type: str) person currently scratching a single position in their lottery ticket
    - ticket_state (type: list): current state of the lottery ticket.
        - Each position corresponds to a position on the lottery ticket
        - Unscratched possitions have "unknown" in that position
        - Scratched positions have the person's name in that position
        - E.g., Imagine that I've scratched off the second position (revealing Robert Crawley's name) and no other positions yet,
          my ticket would look something like: ["unknown", "Robert Crawley", "unknown", "unknown", ..., "unknown"]
    - revealed_names (type: dict): dictionary where keys are the names that this person has revealed so far, and keys are the positions of those names on their ticket
    - scratch_history (type: list): sequence of positions this person has scratched off so far.
        - scratch_history will be empty if they haven't scratched anything off yet (i.e., this call is their first scratch)
        - The length of scratch history tells you how many scratches this person has made so far
        - scratch_history[i] will have this person's i'th scratch
        - scratch_history[-1] will have this person's pervious scratch
    - prepared_info (type: ??): copy of whatever data you generated with your prepare function

    Return value:
    - Return a dictionary with the following keys:
        {"scratch": <position of lottery ticket you want to scratch>, "done": Boolean indicating whether this person wants to quit scratching}
    '''
        # first choice look at our name in the passed in dictionary from prepare
    if len(scratch_history) == 0:
        return {"scratch": prepared_info[name], "done": False}
    
    last_spot = scratch_history[-1]
    persons_name = ticket_state[last_spot]
    if persons_name == name:
        return {"scratch": None, "done": True}
    return {"scratch": prepared_info[persons_name], "done": False}
        # if we do not find our own name check the position from our prepare dict for their position and scratch that one off
        # repeat this until we find our own name
 
