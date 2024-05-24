from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Step 1: Calculate the frequency of each letter in letters
        dictS = {}
        for i in letters:
            dictS[i] = dictS.get(i, 0) + 1

        # Step 2: Helper function to calculate the score of a word
        def word_score(word: str) -> int:
            return sum(score[ord(char) - ord('a')] for char in word)

        # Step 3: Helper function to check if a word can be formed with given letters
        def can_form(word: str, available: Dict[str, int]) -> bool:
            temp = available.copy()
            for char in word:
                if temp.get(char, 0) == 0:
                    return False
                temp[char] -= 1
            return True

        # Step 4: Backtracking function to explore all subsets of words
        def backtrack(index: int, available: Dict[str, int]) -> int:
            if index == len(words):
                return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, available)
            
            # Option 2: Include the current word (if possible)
            current_word = words[index]
            if can_form(current_word, available):
                # Reduce the count of letters
                for char in current_word:
                    available[char] -= 1
                
                # Recur to find the score with this word included
                max_score = max(max_score, word_score(current_word) + backtrack(index + 1, available))
                
                # Restore the count of letters
                for char in current_word:
                    available[char] += 1
            
            return max_score
        
        # Convert letters list to a dictionary with their frequencies
        available_letters = {char: letters.count(char) for char in letters}

        return backtrack(0, available_letters)
        