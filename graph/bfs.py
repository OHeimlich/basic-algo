import queue
import random
from draw_graph import DrawGraph


def bfs(graph, root):
    vertex_q = queue.Queue(len(graph)*2)
    visited = []
    vertex_q.put(root)
    while not vertex_q.empty():
        v = vertex_q.get()
        if v in visited:
            continue
        visited.append(v)
        print(v)
        for vs in graph.get(v, []):
            vertex_q.put(vs)
    return visited




if __name__ == '__main__':
    graph_elements = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F'],
         'C': ['G', 'H', 'I'],
         'D': ['J'],
         'E': ['K', 'L', 'M'],
         'F': ['N', 'O']}
    v = random.choice(list(graph_elements))
    visited = bfs(graph_elements, 'A')
    g = DrawGraph(graph_elements)
    g.show(path=visited)
