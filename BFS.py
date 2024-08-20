from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of the given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:

        bfs_result = []
        visited = [False] * V
        queue = Queue()
        queue.put(0)
        visited[0] = True
        
        while not queue.empty():
            node = queue.get()
            bfs_result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.put(neighbor)
                    visited[neighbor] = True
        
        return bfs_result