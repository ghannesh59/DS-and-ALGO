class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.dic={}
        self.queue=[]
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.dic[key]
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.queue.remove(key)
        elif len(self.dic)==self.capacity:
            val=self.queue.pop(0)
            del self.dic[val]
        self.queue.append(key)
        self.dic[key]=value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)