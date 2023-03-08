mygraph = {
    "Drobeta": [("Craiva", 120), ("Mehadia", 75)],
    "Craiva": [("Drobeta", 120), ("Pitesti", 138), ("Rimnicu Vilcea", 146)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiva", 138), ("Bucharest", 101)]
}


def path_cost(path):
    total_cost = 0
    for(node, cost) in path:
        total_cost = total_cost+cost
    return total_cost, path[0]


def myucs(mygraph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                neighbour_nodes = mygraph.get(node, [])

                for (node2, cost) in neighbour_nodes:
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)
        else:
            continue


answer_path = myucs(mygraph, "Drobeta", "Bucharest")
a, b = path_cost(answer_path)
print("Order of expension = ", answer_path)
print("Shortest path = ", [node for node, cost in answer_path])
print("Total Path cost = ", a)
