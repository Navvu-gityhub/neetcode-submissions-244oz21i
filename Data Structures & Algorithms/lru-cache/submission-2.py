class Node:
    def __init__(self, key, value):
        self.k,self.val=key,value
        self.p=self.n=None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=self.right=Node(0,0)
        self.left.n=self.right
        self.right.p=self.left
    def rmv(self,node):
        prev,nxt=node.p,node.n
        prev.n,nxt.p=nxt,prev
    def ins(self,node):
        prev,nxt=self.right.p,self.right
        prev.n=nxt.p=node
        node.p,node.n=prev,nxt
    def get(self, key: int) -> int:
        if key in self.cache:
            self.rmv(self.cache[key])
            self.ins(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rmv(self.cache[key])
        self.cache[key]=Node(key,value)
        self.ins(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.n
            self.rmv(lru)
            del self.cache[lru.k]