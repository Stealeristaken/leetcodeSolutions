class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for i in s:
            if(i=='('):
                stack.append(i)
            elif(i==')'):
                if(stack==[]):
                    count+=1
                else:
                    stack.pop()
        count+=stack.count('(')
        return count

        