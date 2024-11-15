class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        s=0
        res=1
        i=1
        n=len(arr)
        while i<n and arr[i]>=arr[i-1]:
            i+=1
        if i==n:
            return 0
        i-=1
        e=n-1
        while e>0 and arr[e-1]<=arr[e]:
            e-=1
        def bisect_left(arr,lo,x):
            s=lo
            hi=len(arr)
            while s<hi:
                mid=(s+hi)//2
                if arr[mid]<x:
                    s=mid+1
                else:
                    hi=mid
            return s
        res=i+1
        while i>=0:
            pos=bisect_left(arr,e,arr[i])
            res=max(res,n-pos+i+1,n-e)
            i-=1
        return n-res