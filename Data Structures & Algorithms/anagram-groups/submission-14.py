from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)

        for s in strs:

            key_list = [0] * 26
            for c in s:
                key_list[ord(c) - ord('a')] += 1
            
            hash_map[tuple(key_list)].append(s)

        return list(hash_map.values())