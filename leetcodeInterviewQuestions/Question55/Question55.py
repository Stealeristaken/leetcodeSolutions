class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True

        length=len(nums)
        idx=1
        queue=[]
        queue.append(nums[0])
        while queue:
            jumpLength=queue.pop(0)
            queueLength=len(queue)
            if idx+jumpLength-queueLength>=length:
                return True
            if jumpLength<=queueLength:
                continue

            queue.extend(nums[idx:idx+jumpLength-queueLength])
            idx=idx+jumpLength-queueLength
        return False