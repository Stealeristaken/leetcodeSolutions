from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def move(node, target_value):
            
            for child in node.children:
                if child.value[0] == target_value:

                    child.value[1]=child.value[1]+1
                    return child 
            new_child = Node([target_value,1])
            node.children.append(new_child)  
            return new_child  

        root=Node(None)
        
        for a in range(len(words)):
            node=root
            
            for lev in range(len(str(words[a]))):
                temp=False
                
                node=move(node,str(words[a])[lev])
        
        ans=[]
        for a in words:
            a=str(a)
            node=root
            t=0
            for b in range(len(a)):
                temp=True
                
                for child in node.children:
                
                    if child.value[0] == a[b]:

                        t+=child.value[1]
                        temp=False
                        node=child
                        break
                
                if temp:
                    
                    break
            ans.append(t)
            
        return ans
                