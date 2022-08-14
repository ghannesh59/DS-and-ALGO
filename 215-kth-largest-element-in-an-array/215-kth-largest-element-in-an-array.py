class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(k):
            heap.append(nums[i])
        heapq.heapify(heap)
        for i in range(k,len(nums)):
            heapq.heappush(heap,nums[i])
            heapq.heappop(heap)
        return heap[0]
        