class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums.sort()
        max_freq=0
        count=0
        i=0
        while i <len(nums):
            freq=0
            n=nums[i]
            while i<len(nums) and nums[i]==n:
                freq+=1
                i+=1
            if freq>max_freq:
                max_freq=freq
                count=0
            if freq==max_freq:
                count+=1
        return max_freq*count
  
################################################
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        
        for item in nums:
            if item in freq:
                freq[item]+=1

            else:
                freq[item] = 1
        
        maxFreq = sorted(freq.items(),key=lambda item: item[1],reverse=True)
        
        freqs = []
        
        for i in maxFreq:
            freqs.append(i[1])
        
        maxVal = freqs.count(freqs[0])

        return maxVal * freqs[0]

