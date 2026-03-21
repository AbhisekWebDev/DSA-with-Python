from typing import List

class Solution:
    def dfsRecursive(self, currNode: int, adjMatrix: List[List[int]], visited: List[bool]) -> None:
        # Mark the current node as visited
        visited[currNode] = True

        # Check all possible neighbours
        for neighbour in range(len(adjMatrix[currNode])):
            # If there is a connection (1) AND the neighbour hasn't been visited yet
            if adjMatrix[currNode][neighbour] == 1 and not visited[neighbour]:
                self.dfsRecursive(neighbour, adjMatrix, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        ans = 0

        # Iterate through every node
        for i in range(n):
            if not visited[i]:
                # If we find an unvisited node, it's a new component.
                # The DFS will mark all nodes connected to it as visited.
                self.dfsRecursive(i, isConnected, visited)
                ans += 1

        return ans

# --- Driver Code with Test Cases ---
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: 2 connected components
    # Node 0 and 1 are connected to each other. Node 2 is isolated.
    graph1 = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    print(f"Test Case 1: {solution.findCircleNum(graph1)} | Expected: 2")

    # Test Case 2: 3 connected components
    # No nodes are connected to each other.
    graph2 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(f"Test Case 2: {solution.findCircleNum(graph2)} | Expected: 3")

    # Test Case 3: 1 connected component
    # Node 0 connects to 1. Node 1 connects to both 0 and 2. 
    # Therefore, 0, 1, and 2 are all part of the same component.
    graph3 = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ]
    print(f"Test Case 3: {solution.findCircleNum(graph3)} | Expected: 1")