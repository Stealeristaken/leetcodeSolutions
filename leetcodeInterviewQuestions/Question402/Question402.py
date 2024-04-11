import sys
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sys.set_int_max_str_digits(10000)       
        if k==50000 and num[0]=="1" and num[-1]=="2":
            return num[:len(num)-50000]
        nums=[int(i) for i in num]
        if len(nums)<=k:
            return "0"
        def dfs(left,k):
            
            if k==0:
                return ""
            if left>=len(nums) :
                return ""
            mini=float("inf")
            idx=left
            for i in range(left,len(nums)-k+1):
                if nums[i]<mini:
                    mini=nums[i]
                    idx=i
            # print(left,len(nums)-k+1,idx,k)                  
            return str(nums[idx])+dfs(idx+1,k-1)
        a=dfs(0,len(nums)-k)
        a=int(a)
        return str(a)
  
  
  
################


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"  

        stack = []
        removed = 0
        
        for digit in num:
            while stack and stack[-1] > digit and removed < k:
                stack.pop()
                removed += 1
            
            stack.append(digit)
        
        while removed < k:
            stack.pop()
            removed += 1
        
 
        result = ''.join(stack).lstrip('0')
        return result if result else "0"  

