# Depth first Search or Depth first traversal is a recursive algorithm for 
# searching all the vertices of a graph or tree data structure. 
# Traversal means visiting all the nodes of a graph.

# Depth First Search Algorithm
# A standard DFS implementation puts each vertex of the graph into one of two categories:

# Visited
# Not Visited
# The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

# The DFS algorithm works as follows:

# Start by putting any one of the graph's vertices on top of a stack.
# Take the top item of the stack and add it to the visited list.
# Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
# Keep repeating steps 2 and 3 until the stack is empty.

# Depth First Search Example
# Let's see how the Depth First Search algorithm works with an example.
# We use an undirected graph with 5 vertices.
# graph = {'0': set(['1', '2', '3']),
#          '1': set(['0', '2']),
#          '2': set(['0', '1', '4']),
#          '3': set(['0']),
#          '4': set(['2'])}
# We start from vertex 0, the DFS algorithm starts by putting it in the Visited list and putting all its adjacent vertices in the stack.

# Next, we visit the element at the top of stack i.e. 1 and go to its adjacent nodes.
# Since 0 has already been visited, we visit 2 instead.

# Vertex 2 has an unvisited adjacent vertex in 4,
# so we add that to the top of the stack and visit it.

# After we visit the last element 3, it doesn't have any unvisited adjacent nodes, 
# so we have completed the Depth First Traversal of the graph.

# __________________________________________________

# DFS Pseudocode (recursive implementation)
# The pseudocode for DFS is shown below. In the init() function, notice that we run the DFS function on every node. This is because the graph might have two different disconnected parts so to make sure that we cover every vertex, we can also run the DFS algorithm on every node.

# DFS(G, u)
#     u.visited = true
#     for each v ∈ G.Adj[u]
#         if v.visited == false
#             DFS(G,v)
     
# init() {
#     For each u ∈ G
#         u.visited = false
#      For each u ∈ G
#        DFS(G, u)
# }
# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(visited)

    print(start)

    for next in graph[start] - visited:  # It removes the nodes present in the `visited` set from the set obtained from `graph[start]`
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2', '3']),
         '1': set(['0', '2']),
         '2': set(['0', '1', '4']),
         '3': set(['0']),
         '4': set(['2'])}

dfs(graph, '0')


# Complexity of Depth First Search
# The time complexity of the DFS algorithm is represented in the form of O(V + E), 
# where V is the number of nodes and E is the number of edges.

# The space complexity of the algorithm is O(V).