class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}

        for l in s:
            s_map[l] = s_map.get(l, 0) + 1
        print(s_map)

        for l in t:
            if l not in s_map.keys():
                return False
            s_map[l] = s_map.get(l) - 1 
            if s_map[l] < 0:
                return False
        print(s_map)

        for k in s_map.keys():
            if s_map[k] != 0:
                return False
        return True
            
        