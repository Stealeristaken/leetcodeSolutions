class Solution:
    def groupThePeople(self, nums: List[int]) -> List[List[int]]:
        occur={}
        for i in range(len(nums)):
            if nums[i] not in occur:
                occur[nums[i]]=[i]
            else:
                occur[nums[i]].append(i)
        answer=[]
        for key in occur:
            result=[]
            tmp=occur[key]
            start=0
            div=len(tmp)//key
            for i in range(div):
                answer.append(tmp[start:start+key])
                start+=key
        return (answer)