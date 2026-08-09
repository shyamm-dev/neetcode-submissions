from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        return max(counter.values(), default=0) >= 2