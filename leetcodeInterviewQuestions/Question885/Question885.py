class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        r,c=rStart,cStart
        step=1
        while len(res)<(rows*cols):
            for d in range(4):
                for _ in range(step):
                    if 0<=r<rows and 0<=c<cols:
                        res.append([r,c])
                    r+=direction[d][0]
                    c+=direction[d][1]        
                if d%2==1:
                    step+=1
        return res