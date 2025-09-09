from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        # update
        # insert
        # optionally remove least used


        if key in self.od:
            #update
            self.od[key] = value
            self.od.move_to_end(key)
        
        else:
            #insert
            if len(self.od) == self.capacity:
                #remove least used
                self.od.popitem(last=False)
            self.od[key] = value

