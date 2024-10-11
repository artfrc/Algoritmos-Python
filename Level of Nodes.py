# https://www.geeksforgeeks.org/problems/level-of-nodes-1587115620/1

from queue import Queue

class Solution:
    
    def nodeLevel(self, V, adj, X):
        current_level = 0
        q = Queue()
        q.put(0)
        visited = [False] * V
        visited[0] = True
                
        while not q.empty():
            level_size = q.qsize()
            for _ in range(level_size):
                node = q.get()
                if node == X:
                    return current_level
                
                for neigh in adj[node]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        q.put(neigh)
            current_level += 1
                
        return -1