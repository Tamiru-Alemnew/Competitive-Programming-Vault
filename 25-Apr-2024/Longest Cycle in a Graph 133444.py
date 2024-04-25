# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        num_nodes = len(edges)
        visited = [False] * num_nodes
        longest_cycle_length = -1
      
        for node in range(num_nodes):
            if visited[node]:
                continue
          
            current_node = node
            node_cycle = []
          
            while current_node != -1 and not visited[current_node]:
                visited[current_node] = True
                node_cycle.append(current_node)
                current_node = edges[current_node]
          
            if current_node == -1:
                continue
          
            cycle_length = len(node_cycle)
            cycle_start_index = next((k for k in range(cycle_length) if node_cycle[k] == current_node), float('inf'))
            longest_cycle_length = max(longest_cycle_length, cycle_length - cycle_start_index)
      
        return longest_cycle_length
