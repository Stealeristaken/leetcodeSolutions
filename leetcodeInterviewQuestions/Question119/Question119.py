class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = list()
        if rowIndex==0:
            return [1]
        arr=[[1]]
        for i in range(1, rowIndex+1):
            sub_arr = [1]*(i+1)
            for j in range(1, i):
                sub_arr[j]=arr[i-1][j-1]+arr[i-1][j]
            arr.append(sub_arr)
        return arr[-1]