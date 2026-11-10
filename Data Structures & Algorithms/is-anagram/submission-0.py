class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for s_ch, t_ch in zip(s,t):
            if s_ch in s_count:
                s_count[s_ch] += 1
            else:
                s_count[s_ch] = 1
            if t_ch in t_count:
                t_count[t_ch] += 1
            else:
                t_count[t_ch] = 1
        return s_count == t_count
        
                