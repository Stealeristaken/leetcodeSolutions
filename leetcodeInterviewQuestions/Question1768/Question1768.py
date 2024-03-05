##################### one line but bad submission #####################

class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        return  (w:=''.join([i+j for i,j in zip(w1,w2)]))+max(w1,w2,key=len)[len(w)//2:]
  
  
  
########## more robust submisson


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i, j = 0, 0

        while i< len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i +=1
            j +=1
        
        ans.append(word1[i:])
        ans.append(word2[j:])

        return ''.join(ans)