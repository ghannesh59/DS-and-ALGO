class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        frequency={}
        heap=[]
        ans=[]
        for i in words:
            if i not in frequency:
                frequency[i]=1
            else:
                frequency[i]=frequency[i]+1
        for key,value in frequency.items():
            heap.append((-value,key))
        heapq.heapify(heap)
        while(len(ans)<k):
            val,sol=heapq.heappop(heap)
            ans.append(sol)
        return ans
                
        
        