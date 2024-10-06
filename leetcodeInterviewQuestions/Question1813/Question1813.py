class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        arr1 = sentence1.split(' ')
        arr2 = sentence2.split(' ')

        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        i = 0
        while i < len(arr1) and arr1[i] == arr2[i]:
            i += 1

        j = 0
        while j < len(arr1) - i and arr1[-(j+1)] == arr2[-(j+1)]:
            j += 1

        return i + j == len(arr1)