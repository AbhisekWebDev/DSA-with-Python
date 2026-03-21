from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        [anagram_map["".join(sorted(word))].append(word) for word in strs]
        return list(anagram_map.values())
    
        # alternative using character count as key (more efficient for large strings)
        
        # res = defaultdict(list)
        #     for s in strs:
        #         count = [0] * 26 # a-z
        #         for char in s:
        #             count[ord(char) - ord('a')] += 1
        #         # Convert list to tuple to make it hashable
        #         res[tuple(count)].append(s)
        #     return list(res.values())