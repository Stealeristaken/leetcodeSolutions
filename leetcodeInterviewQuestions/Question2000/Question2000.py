class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char_i in enumerate(word):
            if char_i == ch:
                return word[i::-1] + word[i+1:]
        return word
  
  
########################

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=0
        for i in range(len(word)):
            if word[x]==ch:
                return word[x::-1]+word[x+1:]
            x+=1
        return word

        