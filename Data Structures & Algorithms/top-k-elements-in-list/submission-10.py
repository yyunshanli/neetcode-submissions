import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        data = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        for i, n in freq.items():
            data[n].append(i)
        res = []
        for i in range(len(data) - 1, 0, -1):
            for n in data[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        