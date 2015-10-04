"""
Question:
    LRU Cache

    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Performance:
    1. Total Accepted: 50349 Total Submissions: 328138 Difficulty: Hard
"""

from datetime import datetime


class LRUCacheSlow(object):

    def __init__(self, capacity):
        """
        :type capacity: int

        LRUCache's main requriement is to operate `get` much more than `set`, so `get` operate should costs much less than `set`.
        """
        self.not_exist_value = -1
        self.capacity = capacity
        self.enable_lru = self.capacity > 0

        self.key_get_counters = dict()
        # time is only about operate *sequence*
        self.key_to_touched_time = dict()

        self.store = dict()  # just a simple cache store

    def __repr__(self):
        return "<LRUCache#{} visited status {}, key-value {}>".format(self.capacity, self.key_get_counters, self.store)

    def get(self, key):
        """
        :rtype: int
        """
        val = self.store.get(key, self.not_exist_value)
        if val == self.not_exist_value:
            return self.not_exist_value
        else:
            self.get_lru(key)
            return val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.set_lru(key, value)

    def get_lru(self, key):
        if not self.enable_lru:
            return False

        self.key_get_counters[key] += 1
        self.key_to_touched_time[key] = datetime.now()

    def set_lru(self, key, value):
        if not self.enable_lru:
            return False

        # 0. get current LRU cache status
        curr_size = len(self.store)

        # 1. keep the LRU Cache
        if curr_size < self.capacity:
            pass  # do nothing
        else:
            # need to remove least used item.
            # TODO improve fetch minimal counter performance.
            # select minimal used items in O(N)
            min_count = None
            candidate_keys = []
            # too SLOW!!!
            for k1, c1 in self.key_get_counters.iteritems():
                min_count = min_count or c1
                if c1 < min_count:
                    min_count = c1
                    candidate_keys = [k1]
                else:
                    candidate_keys.append(k1)
            # remove oldest one.
            to_remove_key = sorted(candidate_keys,
                                   key=lambda k1: self.key_to_touched_time[k1])[0]

            # print "LRUCache#{} => remove key:".format(self.capacity), to_remove_key
            del self.store[to_remove_key]
            del self.key_get_counters[to_remove_key]
            del self.key_to_touched_time[to_remove_key]

        # 2. set it!
        self.store[key] = value
        self.key_to_touched_time[key] = datetime.now()
        self.key_get_counters[key] = 0


import collections

class LRUCache:
    """
    copied from http://www.kunxi.org/blog/2014/05/lru-cache-in-python/, it's a nice article.

    Performance:
        Your runtime beats 60.71% of python submissions.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

"""
lc0 = LRUCache(0)
lc0.set("hello", 5)
assert lc0.get("hello") == -1
"""

lc1 = LRUCache(1)
assert lc1.get("hello") == -1
lc1.set("hello", 5)
assert lc1.get("hello") == 5
lc1.set("world", 5)
assert lc1.get("hello") == -1

lc3 = LRUCache(3)
lc3.set("hello", 5)
lc3.set("world", 5)
lc3.set("python", 6)
lc3.set("leetcode", 8)
assert lc3.get("hello") == -1
lc3.set("hello", 5)  # re-insert
assert lc3.get("world") == -1
# current `get` status: hello:0, python:0, leetcode:0
lc3.get("python")
lc3.get("leetcode")
lc3.set("rocks", 5)
# print lc3
assert lc3.get("hello") == -1


# testcase from leetcode testcase
#    2,[set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)]
#    [2,-1]
lc2 = LRUCache(2)
lc2.set(2, 1)
print lc2

lc2.set(2, 2)
print lc2
assert lc2.get(2) == 2
lc2.set(1, 1)
lc2.set(4, 1)
assert lc2.get(2) == -1


"""
-->  LeetCode online judge result <--
Input:
    2,[set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)]

Output:
    [1,-1]

Expected:
    [2,-1]  # => all `get` value
"""
