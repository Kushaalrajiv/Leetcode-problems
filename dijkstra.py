class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        ver = set(range(V))
        distances = {vertex: float('infinity') for vertex in range(V)}
        distances[S] = 0
        
        while ver:
            cur = min(ver, key=lambda v: distances[v]) # finds the minimum distance in the entire vertices
            ver.remove(cur)

            for neighbor, weight in adj[cur]:
                if weight != 9999:  # 9999 is for no edge
                    distance = distances[cur] + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance

        return [distances[i] if distances[i] != float('infinity') else 9999 for i in range(V)]