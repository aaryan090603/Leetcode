class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                i+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                i+=1