"""
Question:
    LRU Cache

    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Performance:
    1. Total Accepted: 50349 Total Submissions: 328138 Difficulty: Hard
"""

from collections import defaultdict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru_list = []  # sorted by high -> low. always sorted when get or set
        self.key_get_counter = defaultdict(int)
        self.key_to_lru_list_idxes = dict()
        self.enable_lru = self.capacity > 0

        self.store = dict()  # just a simple cache store

    def get(self, key):
        """
        :rtype: int
        """
        val = self.store.get(key, -1)
        if val == -1:
            return -1
        else:
            self.get_lru(key)
            return val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        orig_val = self.store.get(key, -1)
        if orig_val == -1:  # then it's a new insert
            self.set_lru(key, value)
        else:
            pass  # do nothing

    def get_lru(self, key):
        if not self.enable_lru:
            return False

        # keep lru list sorted
        self.key_get_counter[key] += 1
        orig_idx = self.key_to_lru_list_idxes[key]
        if orig_idx > 0:  # if equals to zero, then skip this step
            higher_key = self.lru_list[orig_idx - 1]
            higher_key_count = self.key_get_counter[higher_key]
            if higher_key_count >= self.key_get_counter[key]:  # then switch both
                self.lru_list[orig_idx - 1] = key
                self.lru_list[orig_idx] = higher_key
                self.key_to_lru_list_idxes[key] = orig_idx - 1
                self.key_to_lru_list_idxes[higher_key] = orig_idx

    def set_lru(self, key, value):
        if not self.enable_lru:
            return False

        # 1. set it!
        self.store[key] = value

        # 2. keep the LRU Cache
        insert_idx = len(self.lru_list) - 1
        # if insert_idx == -1:  # the first insert into the list
        #    insert_idx = 0
        # Python can't set the idx with value in a list, when the idx not in current list
        use_append = True
        if len(self.lru_list) == self.capacity:  # it's full
            use_append = False

            # remove the (previous) last element information
            to_remove_key = self.lru_list[insert_idx]
            del self.key_get_counter[to_remove_key]
            del self.key_to_lru_list_idxes[to_remove_key]
            del self.store[to_remove_key]

        # replace the last element with current key
        if use_append:
            self.lru_list.append(key)
        else:
            self.lru_list[insert_idx] = key
        self.key_to_lru_list_idxes[key] = insert_idx


lc0 = LRUCache(0)
lc0.set("hello", 5)
assert lc0.get("hello") == -1

lc1 = LRUCache(1)
assert lc1.get("hello") == -1
lc1.set("hello", 5)
assert lc1.get("hello") == 5
lc1.set("world", 5)
assert lc1.get("hello") == -1

lc2 = LRUCache(3)
lc2.set("hello", 5)
lc1.set("world", 5)
lc1.set("python", 6)
lc1.set("leetcode", 8)
assert lc1.get("hello") == -1
# TODO re-insert
