import random


def dfs(graph, root, visited):
    print(root)
    visited.append(root)
    for vs in graph[root]:
        if vs in visited:
            continue
        dfs(graph, vs, visited)

if __name__ == '__main__':
    graph_elements = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    v = random.choice(list(graph_elements))
    dfs(graph_elements, v, [])
