class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        top = sorted(count.items(), key=lambda x:x[1], reverse=True)[:k]
        return [n for n, _ in top]


        