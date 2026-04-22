from visualizer import TreePowerVisualizer

def main():
    # Initialize the visualizer
    viz = TreePowerVisualizer()

    # Step 1: Build the tree from a dictionary
    graph_dict = {
        "A": {"B", "C", "D"},
        "B": {"E", "F"},
        "C": {"G"},
        "D": {"H", "I", "J"},
        "E": {"K"},
        "F": {"L", "M"},
        "G": {"N"},
        "H": {"O", "P"},
        "J": {"Q"},
        "L": {"R"},
        "N": {"S", "T"},
        "P": {"U"}
    }
    viz.load_from_dict(graph_dict)

    # Start the real-time interactive window
    viz.realtime_setup()

    # =======================================================
    # Step 2: Write your algorithm here!
    # =======================================================
    
    # As an example, we will loop through the dictionary keys and 
    # update the UI in real-time as decisions are made.
    
    for node in graph_dict:
        # Wait while "analyzing" to show you the current focus
        viz.realtime_update(f"Algorithm analyzing node: {node}...", pause_time=0.5)
        
        # Pretend your algorithm decides to place a power source at 'A'
        if node == "A":
            viz.set_state("A", "source")
            viz.set_state("B", "powered")
            viz.set_state("C", "powered")
            viz.set_state("D", "powered")
            

    # =======================================================

    # Step 3: Keep the window open when finished
    viz.realtime_update("Algorithm Complete!", pause_time=0.5)
    viz.realtime_keep_open()

if __name__ == "__main__":
    main()
