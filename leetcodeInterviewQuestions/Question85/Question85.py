from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def mah(heights: List[int]) -> int:
            st=[]
            maxArea=0
            for bar in heights+[-1]:
                step=0
                while st and st[-1][1]>=bar:
                    w,h=st.pop()
                    step+=w
                    maxArea=max(maxArea,step*h)
                st.append((step+1,bar))
            return maxArea
        n,m=len(matrix),len(matrix[0])
        ans=0
        height=[0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0
            ans=max(ans,mah(height))
        return ans
    
    
    
######################



def find_maximal_rectangle(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    heights = [0] * (n + 1)
    best = 0
    for row in matrix:
        for col in range(n):
            heights[col] = heights[col] + 1 if row[col] == '1' else 0
        stack = [-1]
        for col in range(n + 1):
            while heights[col] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = col - stack[-1] - 1
                best = max(best, h * w)
            stack.append(col)
    return best
if __name__ == '__main__':
    import json, sys
    with open('user.out', 'w') as f:
        for matrix in map(json.loads, sys.stdin):
            result = find_maximal_rectangle(matrix)
            print(result, file=f)
    sys.exit()