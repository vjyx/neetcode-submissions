class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for stg in strs:
            lng = str(len(stg)) + '!'
            s+= lng + stg
        return s

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            dl = s.find('!', i)
            lng = int(s[i:dl])
            st = dl + 1
            end = st + lng
            txt = s[st:end]
            lst.append(txt)
            i = end
        return lst
