class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        k = 0
        for i,v in enumerate(s):
            if v == '(':
                k += 1
            elif v == ')' and k == 0:
                s[i] = ''
            elif v == ')' and k >0:
                k -= 1
        j = 1
        for i in range(k):
            while s[-j] != '(':
                j += 1
            s[-j] = ''
        return ''.join(s)
        
        
        
########### 

from collections import deque
from typing import List, Deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        1. Process the string and save indexes where a closed paren does not have a matching open one
        2. Check the remaining stack and save indexes of open parens without closed parens
        3. Iterate through the string s again and skip characters with indexes that match invalid chars

        Time: 3*O(N)
        Space: O(N)
        """
        # Push: append() Pop: pop()
        indexes_to_remove: Set[int] = set()
        
        # Stack: index of open paren
        stack: Deque[index] = deque()
        for i in range(len(s)):
            character = s[i]
            if character == "(":
                stack.append(i)
            elif character == ")":
                if (len(stack) > 0):
                    stack.pop()
                # End paren without matching open paren
                else:
                    # Remove this closed paren
                    indexes_to_remove.add(i)

        # Determine which open parens need to be removed
        while(len(stack) > 0):
            index = stack.pop()
            indexes_to_remove.add(index)
        
        # Reprocess the string and remove the characters that cause invalidity
        result = ""
        for i in range(len(s)):
            if i in indexes_to_remove:
                continue
            result += s[i]

        return result

        