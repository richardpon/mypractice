import unittest
from lru_cache import LRUCache
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    

    def test_cache(self):
        cache = LRUCache(3)
        cache.put(1,1)
        cache.put(2,2)
        cache.put(3,3)

        #recency[2,3,1]
        ret = cache.get(1)
        self.assertEquals(ret, 1)

        ret = cache.get(5)
        self.assertEquals(ret, -1)

        #recency[3,1,4]
        cache.put(4,4)
        ret = cache.get(2)
        self.assertEquals(ret, -1)

        #recency[3,4,1]
        ret = cache.get(1)
        self.assertEquals(ret, 1)

        #recency[4,1,5]
        cache.put(5,5)

        #recency[1,5,6]
        cache.put(6,6)

    def test2(self):
        cache = LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        self.assertEquals(cache.get(1), 1)
        cache.put(3,3)
        self.assertEquals(cache.get(2), -1)
        cache.put(4,4)
        self.assertEquals(cache.get(1), -1)
        self.assertEquals(cache.get(3), 3)
        self.assertEquals(cache.get(4), 4)

if __name__ == '__main__':
    unittest.main()
