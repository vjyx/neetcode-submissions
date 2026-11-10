class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for s_ch, t_ch in zip(s,t):
            s_count[s_ch] = s_count.get(s_ch, 0) + 1
            t_count[t_ch] = t_count.get(t_ch, 0) + 1
        return s_count == t_count
        
                