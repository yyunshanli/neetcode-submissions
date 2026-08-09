class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_maps = defaultdict(list)

        for s in strs:
            m = [0] * 26
            for l in s:
                m[ord(l)-ord('a')] += 1

            unique_maps[tuple(m)].append(s)

        return list(unique_maps.values())

        