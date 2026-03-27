from collections import deque


class Solution:
    def firstUniqChar(self, s: str) -> int:

        char_counts = {}
        queue = deque()
        
        for i, char in enumerate(s):
            # 1. Update the frequency of the current character
            char_counts[char] = char_counts.get(char, 0) + 1
            
            # 2. Add the character and its index to the queue
            queue.append((char, i))
            
            # 3. Clean up the front of the queue
            # If the character at the front of the queue is repeating, remove it
            while queue and char_counts[queue[0][0]] > 1:
                queue.popleft()
                
        # 4. Result evaluation
        # If the queue is not empty, the front holds the first unique character
        if queue:
            return queue[0][1]
            
        return -1
        