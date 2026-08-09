class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1

        top = sorted(res.items(), key=lambda x: x[1], reverse=True)[:k]

        return [num for num, _ in top]

            
        