from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        hashmap = []
        for key, v in freq.items():
            heapq.heappush(hashmap, (-v, key))
        
        out = []
        while k:
            out.append(heapq.heappop(hashmap)[1])
            k -= 1
        return out