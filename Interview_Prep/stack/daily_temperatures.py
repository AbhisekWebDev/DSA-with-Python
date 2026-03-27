from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)) :
            current_temp = temperatures[i]
        
        # While stack is not empty AND current day is warmer than the day at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day_index = stack.pop()
                # Calculate how many days we waited
                ans[prev_day_index] = i - prev_day_index
                
            # Add the current day to the stack to wait for a warmer day
            stack.append(i)

        return ans

        