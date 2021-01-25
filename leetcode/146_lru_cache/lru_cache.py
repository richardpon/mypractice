"""
get is O(1)
put is O(n) if already in cache
  must find item and put at end of recents
  O(1) if not in cache and has capacity
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recents = []   # append new access, index=0 oldest        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_recency(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
    
        if not key in self.cache:
        
            if self.capacity > 0:    
                # track it    
                self.capacity -= 1
            
            else:
                #evict oldest, replace it
                oldest = self.recents[0]
                self.recents.remove(oldest)
                self.cache.pop(oldest,None)

        # always add to cache (or overwrite)    
        self.cache[key] = value

        #make it most recent
        self.update_recency(key)

    def update_recency(self, key):
        if key in self.recents:
            self.recents.remove(key)
        self.recents.append(key)
 



        

