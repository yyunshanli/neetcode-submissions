class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s))+ "#"  + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        count = ""
        i = 0
        while i < len(s):
            while(s[i] != '#'):
                count += s[i]
                i+=1;
                continue
            start = i + 1
            end = start + int(count)
            res.append(s[start:end])
            i = end
            count = ""
        return res
