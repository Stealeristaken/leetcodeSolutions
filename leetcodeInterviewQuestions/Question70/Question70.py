class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=3:
            return n
        steps=[0,1,2]
        for i in range (3,n+1):
            currentStep=steps[2]+steps[1]
            steps[2],steps[1],steps[0]=currentStep,steps[2],steps[1]

        return steps[2]