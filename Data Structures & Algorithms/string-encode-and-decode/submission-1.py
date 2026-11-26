class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}!{s}')
        return "".join(res)

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
