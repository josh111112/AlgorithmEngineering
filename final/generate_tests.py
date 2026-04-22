import random
def write_graph(filename, v, e, graph_type='random'):
    with open(filename, 'w') as f:
        edges = set()
        if graph_type == 'random':
            while len(edges) < e:
                u = random.randint(0, v-1)
                w = random.randint(0, v-1)
                if u != w:
                    if u > w:
                        u, w = w, u
                    edges.add((u, w))
        elif graph_type == 'cycle':
            for i in range(v):
                edges.add((i, (i+1)%v))
        elif graph_type == 'star':
            for i in range(1, v):
                edges.add((0, i))
        
        f.write(f"{v} {len(edges)}\n")
        for u, w in edges:
            f.write(f"{u} {w}\n")

write_graph('test_size_12.txt', 12, 16, 'random')
write_graph('test_size_18.txt', 18, 25, 'random')
write_graph('test_size_21.txt', 21, 30, 'random')
