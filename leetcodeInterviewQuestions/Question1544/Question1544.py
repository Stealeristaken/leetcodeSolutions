class Solution:
    def makeGood(self, s: str) -> str:
        arr=""
        i=0
        while(i<len(s)-1):
            if ord(s[i])==ord(s[i+1])+32 or ord(s[i])+32==ord(s[i+1]):
                arr=s[:i]+s[i+2:]
                if(i==0):
                    i-=1
                else:
                    i-=2
                s=arr
            i+=1
        return s
  
  
  
#################### 

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                if char.lower() == stack[-1].lower() and char != stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)
        