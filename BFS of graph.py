# https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?ref=gcse_outind

from typing import List
from queue import Queue

class Solution:
    
  def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
    ans = []
    visited = [False] * V
    q = Queue()
    
    q.put(0)
    visited[0] = True
    while not q.empty():
      node = q.get()
      ans.append(node)
      
      for neighbor in adj[node]:
        if not visited[neighbor]:
          q.put(neighbor)
          visited[neighbor] = True
        
    return ans
    

      
