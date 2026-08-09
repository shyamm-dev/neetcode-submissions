from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map = defaultdict(int)

        for i in s:
            hash_map[i] += 1
        
        for i in t:
            hash_map[i] -= 1
        
        return not max(hash_map.values())