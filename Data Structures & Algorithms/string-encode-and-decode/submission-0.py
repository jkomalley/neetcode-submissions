class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s):0>3}{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        ret = []

        index = 0

        while index < len(s):
            cur_len = int(s[index:index+3])
            
            index = index + 3

            ret.append(s[index:index+cur_len])

            index += cur_len
        
        return ret
