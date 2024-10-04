# Traversal means visiting all the nodes of a graph. Breadth First Traversal or Breadth First Search is a recursive algorithm 
# for searching all the vertices of a graph or tree data structure.

# BFS algorithm
# A standard BFS implementation puts each vertex of the graph into one of two categories:

# 1. Visited
# 2. Not Visited
# The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

# The algorithm works as follows:

# 1. Start by putting any one of the graph's vertices at the back of a queue.
# 2. Take the front item of the queue and add it to the visited list.
# 3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
# 4. Keep repeating steps 2 and 3 until the queue is empty.
# The graph might have two different disconnected parts so to make sure that we cover every vertex, 
# we can also run the BFS algorithm on every node

# BFS example
# Let's see how the Breadth First Search algorithm works with an example. 
# We use an undirected graph with 5 vertices.
# graph = {
#         0: [3, 2, 1], 
#         1: [0, 2], 
#         2: [0, 1, 4], 
#         3: [0],
#         4: [2]
#     }
# We start from vertex 0, the BFS algorithm starts by putting it in the Visited list and putting all its adjacent vertices in the stack.

# Next, we visit the element at the front of queue i.e. 1 and go to its adjacent nodes. Since 0 has already been visited, we visit 2 instead.
# Vertex 2 has an unvisited adjacent vertex in 4, so we add that to the back of the queue and visit 3, which is at the front of the queue.
# Only 4 remains in the queue since the only adjacent node of 3 i.e. 0 is already visited. We visit it.
# Since the queue is empty, we have completed the Breadth First Traversal of the graph.

# BFS pseudocode

# create a queue Q 
# mark v as visited and put v into Q 
# while Q is non-empty 
#     remove the head u of Q 
#     mark and enqueue all (unvisited) neighbours of u

# BFS algorithm in Python


# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), [root]
    visited.add(root)
 
    while queue:

        # Dequeue a vertex from queue
        vertex = queue.pop(0)
        print(str(vertex) + " ", end="\n")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {
            0: [3, 2, 1], 
            1: [0, 2], 
            2: [0, 1, 4], 
            3: [0],
            4: [2]
        }
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)


# BFS Algorithm Complexity
# The time complexity of the BFS algorithm is represented in the form of O(V + E), 
# where V is the number of nodes and E is the number of edges.

# The space complexity of the algorithm is O(V)