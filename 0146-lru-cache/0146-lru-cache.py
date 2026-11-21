class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capa = capacity
        self.lru = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru:
            v = self.lru.pop(key)
            self.lru[key] = v
            return self.lru.get(key)
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.lru) == self.capa and key not in self.lru:
            self.lru.popitem(last=False)
        if key in self.lru:
            del self.lru[key]
        self.lru[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)