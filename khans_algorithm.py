import queue

def get_degree(edges:list, node:int) -> int:
    count:int = 0

    for edge in edges:
        if node == edge[1]:
            count += 1

    return count

def get_degrees(edges:list, nodes:list) -> list:
    degrees:dict = {}

    for node in nodes:
        degree:int = get_degree(edges, node)
        degrees = {node: degree} | degrees

    return degrees

def get_queue(degrees):
    q = queue.Queue()

    for degree in degrees.items():
        if degree[1] == 0:
            q.put(degree[0])

    return q

def get_edges(edges, node):
    node_edges:list = []

    for edge in edges:
        if edge[0] == node:
            node_edges.append(edge)

    return node_edges

def main():
    edges = [(9,2), (9,10), (2,6), (10, 6), (0,2), (0,6), (0,3), (6,11), (6,7), (3,1), (3,4), (1,4), (4,5), (4,8), (11,12), (7,12), (7,4), (12, 8)]
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    degrees = get_degrees(edges, nodes)
    q = get_queue(degrees)
    l = []

    while not q.empty():
        node = q.get() 
        l.append(node)
        node_edges:list = get_edges(edges, node)
        for edge in node_edges:
            degrees[edge[1]] -= 1
            if (degrees[edge[1]] == 0):
                q.put(edge[1])

    print(l)

main()
