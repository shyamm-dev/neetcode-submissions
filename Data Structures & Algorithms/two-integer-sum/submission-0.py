from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)

        for i, v in enumerate(nums):
            if v in hash_map:
                return [hash_map[v], i]
            hash_map[target - v] = i
        return []