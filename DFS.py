class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        dfs_result = []
        visited = [False] * V
        stack = []
        stack.append(0)
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                dfs_result.append(node)

                for neighbor in reversed(adj[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return dfs_result