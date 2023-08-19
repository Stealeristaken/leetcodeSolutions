'''

    This python file is about regular  leet code questions. I won't write description of questions.
You will see solutions and question names and their numbers.

    !!İf that helped you a bit please drop a star you're welcomed ^^!!

'''

# Question 1 - Two Sum:

class Solution:
    def twoSum(self, nums, target):
        # Create a hash table to store the indices of the elements
        hash_table = {}

        # Iterate through the list of nums
        for i, num in enumerate(nums):
            # Check if target - num is in the hash table
            if target - num in hash_table:
                # If it is, return the indices of the two numbers
                return [hash_table[target - num], i]
            # Otherwise, add the current element and its index to the hash table
            hash_table[num] = i

        # If we reach here, it means we didn't find a solution
        return []

####################################################################################################################################

#Question 2 - Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to store the result
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Iterate until both linked lists are not empty
        while l1 or l2:
            # Get the values of the current nodes in the linked lists
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum and the carry
            sum = x + y + carry
            carry = sum // 10
            sum %= 10

            # Create a new node with the sum as its value
            current.next = ListNode(sum)
            current = current.next

            # Move to the next nodes in the linked lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there is a carry left, add it to the result
        if carry:
            current.next = ListNode(carry)

        # Return the result without the dummy node
        return dummy.next

####################################################################################################################################

#Question 3 - Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize the result and the sliding window
        result = 0
        window = set()

        # Initialize the left and right pointers of the sliding window
        left = 0
        right = 0

        # Iterate until the right pointer reaches the end of the string
        while right < len(s):
            # Check if the character at the right pointer is not in the window
            if s[right] not in window:
                # If it is not, add it to the window and move the right pointer
                window.add(s[right])
                right += 1
                # Update the result if necessary
                result = max(result, right - left)
            else:
                # If it is, remove the character at the left pointer from the window and move the left pointer
                window.remove(s[left])
                left += 1

        # Return the result
        return result

####################################################################################################################################

#Question 4 - Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

####################################################################################################################################
#Question 5 - Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        l = 0
        r = 1

        while r <= len(s):
            if s[l:r] != s[l:r][::-1]:
                if l > 0 and s[l - 1:r] == s[l - 1:r][::-1]:
                    l -= 1
                else:
                    while l < r and s[l:r] != s[l:r][::-1]:
                        l += 1
            res = s[l:r] if len(res) < len(s[l:r]) else res
            r += 1
        return res

####################################################################################################################################
#Question 6 - Zig-Zag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycle_length = 2 * (numRows - 1)
        result_rows = [""] * numRows

        apply_to_result = lambda i, row: result_rows.__setitem__(row, result_rows[row] + s[i])

        for i, c in enumerate(s):
            row = i % cycle_length
            row = cycle_length - row if row >= numRows else row
            apply_to_result(i, row)

        return "".join(result_rows)

####################################################################################################################################
#Question 7 - Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        # Define a flag for handling negative numbers
        negative_flag = False
        if x < 0:
            negative_flag = True
            x = abs(x)

        # Reverse the digits
        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        # Apply the negative sign if needed
        if negative_flag:
            reversed_x = -reversed_x

        # Check if the reversed number is within the 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x

####################################################################################################################################
#Question 8 - String to Integer (atoi)

class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value

####################################################################################################################################
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

####################################################################################################################################
# Question 10 - Regular Expression Matching

class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]

        dp[0][0] = True

        for i in range(1, len(dp)):
            if p[i - 1] == '*' and i > 1:
                dp[i][0] = dp[i - 2][0]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                if p[i - 1] == '*':
                    if p[i - 2] == '.' or p[i - 2] == s[j - 1]:
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]

        return dp[-1][-1]

####################################################################################################################################
# Question 11 - Container with Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=m=0
        r=len(height)-1
        while l<r:
            if height[l]>height[r]:
                a=height[r]*(r-l)
                if a>m:
                    m=a
                r-=1

            else:
                a = height[l]*(r-l)
                if a>m:
                    m=a
                l+=1
        return m

####################################################################################################################################
# Question 12 - Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Roman=""
        storeIntRoman=[[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman+=storeIntRoman[i][1]
                num-=storeIntRoman[i][0]
        return Roman