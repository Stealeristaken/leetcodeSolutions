class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
       i=0
       j=0
       
       while i<len(nums1) and j<len(nums2):
           if nums1[i]==nums2[j]:
               if nums1[i]==nums2[j]:
                   return nums1[i]
           elif nums1[i]<nums2[j]:
               i=i+1
           else:
               j=j+1
       return -1   
 
 
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1 = index2 = 0
        length1, length2 = len(nums1), len(nums2)
        while index1 < length1 and index2 < length2:
            if nums1[index1] == nums2[index2]:
                return nums1[index1]
            if nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
        return -1