class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n=='1':
            return '0'
        length=len(n)
        palindromes=set()
        prefix=n[:(length+1)//2]
        prefix_num=int(prefix)
        for i in [-1,0,1]:
            new_prefix=str(prefix_num+i)
            if length%2==0:
                candidate=new_prefix+new_prefix[::-1]
            else:
                candidate=new_prefix+new_prefix[:-1][::-1]
            palindromes.add(candidate)
        palindromes.add(str(10**(length-1)-1))
        palindromes.add(str(10**(length)+1))
        palindromes.discard(n)
        res = min(palindromes,key=lambda x:(abs(int(x)-int(n)),int(x)))
        return res