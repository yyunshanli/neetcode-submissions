class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            a_map = [0] * 26
            for letter in word:
                a_map[ord(letter)- ord('a')] += 1
            res[tuple(a_map)].append(word)

        return list(res.values())

            



        