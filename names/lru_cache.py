from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.

    Sounds like a queue
    When a pair is updated or newly set the other pairs in cache is now one spot lower (array sounds good here)
    If cache is at maximum lowest gets removed
    If key exists overwrite 
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.nodes = 0
        self.dll = DoublyLinkedList()
        # fast access sounds like array
        self.storage = {}

    def __str__(self):
        return f"Cache: {repr(self.storage)}"
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if hasattr(self.storage, key):
        if key in self.storage:
            # move to end of linkedlist
            print("yes")
            node = self.storage[key]
            self.dll.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        print(self.storage.get(key))
        if self.nodes == self.limit:
            # print("max cache")
            del self.storage[self.dll.remove_from_head()[0]]
            node = self.dll.remove_from_head()
            # [[k, v]] = node.items()
            # print("sup", k, v)
            # self.storage.pop(k)
            # del self.storage[self.dll.remove_from_head().value[0]]

            self.dll.add_to_tail({key: value})
            self.storage[key] = value
        
        if self.storage.get(key) is not None:
            print("overwrite")
            node = self.storage[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
            # self.storage[key] = value had this originally
            # self.dll.move_to_end({key: value})
        else:
            # print("adding")
            self.dll.add_to_tail((key, value))
            self.storage[key] = self.dll.tail
            self.nodes += 1
            # self.storage[key] = value # what I had originally

my_cache = LRUCache()
# print(my_cache.dll.add_to_tail(10))
# print(my_cache.dll.add_to_tail(4))
# print(my_cache.dll.add_to_tail(25))
# print(my_cache.dll.add_to_tail(14))
my_cache.set("boo", "aaa")
my_cache.set("bob", "builder")
my_cache.set("bob", "bro")

print(my_cache.get("boo"))


# print(my_cache)

# print(my_cache.storage)