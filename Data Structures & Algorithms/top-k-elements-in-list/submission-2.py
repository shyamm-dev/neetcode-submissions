from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        hashmap = []
        for key, v in freq.items():
            heapq.heappush(hashmap, (v, key))
            if len(hashmap) > k:
                heapq.heappop(hashmap)
        
        out = []
        while len(hashmap):
            out.append(heapq.heappop(hashmap)[1])
        return out