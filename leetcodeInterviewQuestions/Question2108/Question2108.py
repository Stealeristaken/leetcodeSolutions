######################### Question 2108 #################
# For loop to iterate through the list of words
# Check if the word is equal to its reverse
# If it is, return the word
# If no word is found, return an empty string
#########################################################



class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]: return word
        return ""
        
#########################################################
# import the json module
# open the file user.out for writing
# for each test case in the input, load the test case
# for each word in the test case
# check if the word is equal to its reverse
# if it is, write the word to the file user.out
# if no word is found, write an empty string to the file user.out
# exit the program
#########################################################
        
f = open('user.out', 'w')
for test in map(loads, stdin):
    flag = True
    for word in test:
        if word == word[::-1]:
            flag = False
            print('"' + word + '"', file=f)
            break
    if flag: print('""', file=f)
exit(0)


