class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capa = capacity
        self.lru = {}
        self.cnt = 0
        self.check = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru:
            self.cnt += 1
            self.check[key] = self.cnt
            return self.lru[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.lru[key] = value
        self.cnt += 1
        self.check[key] = self.cnt
        items = self.check.items()
        if len(items) > self.capa:
            items = sorted(items, key = lambda x: x[1])
            del self.lru[items[0][0]]
            del self.check[items[0][0]]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)