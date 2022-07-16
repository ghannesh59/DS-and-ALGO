class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            val=nums.index(0)
            nums.pop(val)
            prod=math.prod(nums)
            nums.insert(val,prod)
            for i in range(len(nums)):
                if i!=val:
                    nums[i]=0
            return nums
        product=1
        for i in nums:
            product=product*i
        for i in range(len(nums)):
            nums[i]=int(product/nums[i])
        return nums