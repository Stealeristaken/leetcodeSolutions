class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char_i in enumerate(word):
            if char_i == ch:
                return word[i::-1] + word[i+1:]
        return word