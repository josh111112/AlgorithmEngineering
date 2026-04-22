import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class TreePowerVisualizer:
    def __init__(self):
        self.graph = nx.Graph()
        self.states = {} # node -> state ('unpowered', 'source', 'powered')
        self.history = [] # list of (states_dict, message) for each step
        self.pos = None
        
        # Real-time state
        self.fig = None
        self.ax = None
        self.is_realtime = False

    def load_from_dict(self, adj_dict):
        """Build the tree from an adjacency dictionary format like {'A': {'B', 'C'}, 'B': {'D'}}"""
        for u, neighbors in adj_dict.items():
            if u not in self.states:
                self.states[u] = 'unpowered'
                self.graph.add_node(u)
            for v in neighbors:
                self.add_edge(u, v)

    def add_edge(self, u, v):
        """Add an edge between u and v to construct the tree."""
        self.graph.add_edge(u, v)
        if u not in self.states:
            self.states[u] = 'unpowered'
        if v not in self.states:
            self.states[v] = 'unpowered'

    def set_state(self, node, state):
        """
        Set the state of a node. 
        Valid states:
          - 'unpowered': Not powered (gray)
          - 'source': Node has a power source (gold)
          - 'powered': Node is powered by an adjacent source (skyblue)
        """
        if state not in ['unpowered', 'source', 'powered']:
            raise ValueError(f"Invalid state: {state}")
        
        self.states[node] = state

    def _get_node_color(self, state):
        if state == 'unpowered':
            return '#d3d3d3' # lightgray
        elif state == 'source':
            return '#ffd700' # gold
        elif state == 'powered':
            return '#87ceeb' # skyblue
        return 'white'

    def _generate_layout(self):
        """Generates a layout for the graph. Fallback to spring layout."""
        if self.pos is None:
            self.pos = nx.spring_layout(self.graph, seed=42)
        return self.pos

    # ========================================================
    # ANIMATION MODE METHODS (End-of-script playback)
    # ========================================================
    
    def record_step(self, message=""):
        """Save the current state of the tree to the history for animation."""
        self.history.append((self.states.copy(), message))

    def show(self):
        """Show a static plot of the final/current state."""
        pos = self._generate_layout()
        colors = [self._get_node_color(self.states[n]) for n in self.graph.nodes()]

        plt.figure(figsize=(10, 8))
        nx.draw(self.graph, pos, with_labels=True, node_color=colors, 
                node_size=1500, font_weight='bold', font_size=12, edge_color='gray')
        plt.title("Final State", fontsize=16)
        plt.show()

    def show_animation(self, interval=1500):
        """
        Show an animated progression of your algorithm.
        interval: milliseconds between frames.
        """
        if not self.history:
            print("No history to animate.")
            return

        pos = self._generate_layout()
        fig, ax = plt.subplots(figsize=(10, 8))

        def update(frame_idx):
            ax.clear()
            states_dict, msg = self.history[frame_idx]
            colors = [self._get_node_color(states_dict[n]) for n in self.graph.nodes()]
            
            nx.draw(self.graph, pos, ax=ax, with_labels=True, node_color=colors, 
                    node_size=1500, font_weight='bold', font_size=12, edge_color='gray')
            ax.set_title(f"Step {frame_idx + 1}/{len(self.history)}: {msg}", fontsize=16)

        anim = FuncAnimation(fig, update, frames=len(self.history), interval=interval, repeat=False)
        plt.show()

    # ========================================================
    # REAL-TIME MODE METHODS (Updates as your algorithm runs)
    # ========================================================

    def realtime_setup(self):
        """Call this before your algorithm starts to open the live window."""
        plt.ion() # Turn on interactive mode
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.is_realtime = True
        self.realtime_update("Starting Algorithm...")

    def realtime_update(self, message="", pause_time=1.5):
        """
        Call this every time your algorithm makes a step to redraw the window.
        pause_time: seconds to wait before continuing the script.
        """
        if not self.is_realtime:
            print("Warning: Called realtime_update without calling realtime_setup first!")
            return

        pos = self._generate_layout()
        colors = [self._get_node_color(self.states[n]) for n in self.graph.nodes()]
        
        self.ax.clear()
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_color=colors, 
                node_size=1500, font_weight='bold', font_size=12, edge_color='gray')
        self.ax.set_title(message, fontsize=16)
        
        # Redraw and pause script execution briefly
        plt.draw()
        plt.pause(pause_time)

    def realtime_keep_open(self):
        """Call this at the very end of your script so the window stays open."""
        if self.is_realtime:
            plt.ioff() # Turn off interactive mode so plt.show() blocks
            plt.show()
