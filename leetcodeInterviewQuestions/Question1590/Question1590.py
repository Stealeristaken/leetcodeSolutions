class Solution:
    def prev_remain(self,cur_remain, total_remain, p):
        prev = cur_remain - total_remain
        return prev if prev>=0 else (prev+p)
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_remain_dict = defaultdict(int)
        min_remove = len(nums) + 1
        prefix_remain_dict[0] = 0
        remain = sum(nums)%p
        prev_prefix_remain = 0
        if remain == 0:
            return 0
        for i in range(1,len(nums)+1):
            cur_remain = (prev_prefix_remain + nums[i-1])% p
            prefix_remain_dict[cur_remain] = i
            prev_remain = self.prev_remain(cur_remain, remain, p)
            if prev_remain in prefix_remain_dict:
                min_remove = min(min_remove, i-prefix_remain_dict[prev_remain])
            prev_prefix_remain = cur_remain

        return min_remove if min_remove < len(nums) else -1
        