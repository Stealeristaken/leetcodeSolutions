# Question 9 - Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        input_num=x
        new_num=0
        while x>0:
            new_num=new_num*10+x%10
            x//=10
        return new_num==input_num