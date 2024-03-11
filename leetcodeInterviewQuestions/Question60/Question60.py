'''
Approach
Consider the example: n = 3, k = 3. The result is 213.
Let's think about how to obtain 213 given k=3.
The total number of permutation is n! = 3! = 6.

Observation:
The number of permutation that start with digit 1/2/3 are all (n-1)!=2!.
If k = 1 or 2, we know the result must be started by digit 1; if k = 3 or 4, the first digit in the result is 2; if k = 5 or 6, the first digit must be 3.

By this observation, we can decide what the first digit in the result should be.
In this example, the first digit is 2. Now we now subtract 2 from k, and now k becomes 1.
This is because we will find our results from cases that start with 2, and we ignore all the cases that start with 1 and there are totally 2 cases that start with 1.

There are 2 cases associated with permutations that start with 2: 213 and 231.
To get the second digit, we consider the permutations of this list [1,3].
Notice that the permutations can start with either 1 or 3; and for both digits,
there are only (n-1)!=1!=1 permutation, where n is the length of the list.
Notice now k is 1, which implies the digit is 1.
So we have obtained our second digit as 2.

The last digit is decided more easily since there are only one digit remains in the list:
if n==1, return the only digit in the list directly.

Notice that the step of deciding each digit is similar, so we use recursion to solve the problem.
Also, you might be more comfortable to do the matrix indexing if k is 0-indexed.
'''

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i + 1 for i in range(n)]
        return self.getPermutation2(k - 1, nums)  # we want k be 0-indexed

    def getPermutation2(self, k, nums) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if k == 0: return "".join([str(i) for i in nums])  # shortcut for speeding up
        p_n_1 = math.factorial(n - 1)  # permutations of n-1
        idx = k // p_n_1  # idx of the chosen digit
        return str(nums[idx]) + self.getPermutation2(k % p_n_1, nums[:idx] + nums[idx + 1:])

