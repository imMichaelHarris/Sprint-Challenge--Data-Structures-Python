class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def delete(self):
    if self.prev:
        self.prev.next = self.next
    if self.next:
        self.next.prev = self.prev

class DoubleLinkedList:
  def __init__(self, node= None):
    self.head = node
    self.tail = node

  def add_to_tail(self, value):
    new_node = ListNode(value)
    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

  def remove_from_tail(self):
    value = self.tail.value
    self.delete(self.tail)
    return value

  def delete(self, node):
    if self.head is self.tail:
      self.head = None
      self.tail = None
    elif self.head is node:
      self.head = node.next
      node.delete()
    elif self.tail is node:
      self.tail = node.prev
      node.delete()
    else:
      node.delete()

class Stack:
  def __init__(self):
    self.size = 0
    self.storage = DoubleLinkedList()

  def push(self, value):
    self.storage.add_to_tail(value)
    self.size += 1
    return value

  def pop(self):
    self.size -= 1
    return self.storage.remove_from_tail()

  def len(self):
    return self.size

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

    # Similar to the LRU Cahce but we don't have to switch orders around
    # A Stack would be good here because we always want to append at the end of the buffer
    # Can use and array also because if we want to delete we just delete the first element in the list
    # Use list comprehension to not return none values

  def append(self, item):
    pass

  def get(self):
    pass