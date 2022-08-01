class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forw=[1 for i in range(len(nums))]
        backw=[1 for i in range(len(nums))]
        for i in range(len(nums)-1):
            forw[i+1]=nums[i]*forw[i]
        n=len(nums)-1
        while(n>0):
            backw[n-1]=nums[n]*backw[n]
            n=n-1
        for i in range(len(nums)):
            nums[i]=forw[i]*backw[i]
        return nums