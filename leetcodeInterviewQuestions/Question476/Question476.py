class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)[2:]
        v=str(s)
        l=[]
        for i in v:
            if i=="0":
                l.append("1")
            else:
                l.append("0")
        v=''.join(l)
        b=int(v,2)
        return b