class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic={}
        self.head=Node(0,0)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
       
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node=self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node=self.dic[key]
            self.remove(node)
        else:
            if len(self.dic)>=self.capacity:
                self.removefromtail()
        node=Node(key,value)
        self.dic[key]=node
        self.add(node)
            
            
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def add(self,node):
        head_next=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=head_next
        head_next.prev=node
    
    def removefromtail(self):
        if len(self.dic)==0:return
        node=self.tail.prev
        del self.dic[node.key]
        self.remove(node)
                
       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)