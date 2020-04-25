class LRUCache:
    def __init__(self,capacity):
        self.size = capacity
        self.age = 0
        self.dic = {} 

    def put(self,key,value): 
        self.age += 1
        if len(self.dic) != self.size:
            cache = Cache(key,value,self.age) 
            self.dic[key] = cache 
        else:
            if key in self.dic: 
                self.dic[key] = Cache(key,value,self.age) 
            else:
                min_cache = min(self.dic,key=lambda x:self.dic[x].age)
                
                self.dic.pop(min_cache)
                self.dic[key] = Cache(key,value,self.age) 
                

    def get(self, key):
        if key in self.dic:
            value = self.dic[key].value 
            self.put(key,value)
            return value
        else:
            return -1

class Cache:
    def __init__(self,key,value,age):
        self.key=key
        self.value=value
        self.age = age
 
cache = LRUCache(2)
print([cache.put(1,1),
cache.put(2,2),
cache.get(1),
cache.put(3,3),
cache.get(2),
cache.put(4,4),
cache.get(1),
cache.get(3),
cache.get(4)])
