from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If 'merged' is empty or no overlap with the last interval
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval with the last one
                # We take the max of the end times
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
        