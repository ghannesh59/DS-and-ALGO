class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p=random.choice(nums)
        l=[x for x in nums if x<p]
        m=[x for x in nums if x==p]
        r=[x for x in nums if x>p]
        if k<=len(r):
            return self.findKthLargest(r,k)
        elif (k - len(r)) <= len(m):
            return m[0]
        else:
            return self.findKthLargest(l, k - len(r) - len(m))