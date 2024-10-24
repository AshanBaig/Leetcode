class LRUCache:
    def __init__(self, capacity: int):
        self.LRU={}
        self.cache=[]
        self.capacity=capacity
    def get(self, key: int) -> int:
        if key in self.LRU:
            self.cache.remove(key)
            self.cache.append(key)
            return self.LRU[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key not in self.LRU:
            if len(self.LRU)+1>self.capacity:
                del self.LRU[self.cache.pop(0)]
            self.cache.append(key)
            self.LRU[key]=value
        else:
            self.cache.remove(key)
            self.cache.append(key)
            self.LRU[key]=value