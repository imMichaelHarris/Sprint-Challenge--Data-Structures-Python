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

  def add_to_head(self, value):
    new_node = ListNode(value)
    if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


  def add_to_tail(self, value):
    new_node = ListNode(value)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def move_to_front(self, node):
    if node is self.head:
      return
    if str(node):
      node = ListNode(node)
    value = node.value
    self.delete(node)
    self.add_to_head(value)

  def remove_from_head(self):
    value = self.head.value
    self.delete(self.head)
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

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.queue = DoubleLinkedList()

    # Similar to the LRU Cahce but we don't have to switch orders around
    # A Queue would be good here because we always want to append at the end of the buffer
    # Can use and array also because if we want to delete we just delete the first element in the list
    # Use list comprehension to not return none values

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0
      self.queue.move_to_front(item)
      self.storage[self.current] = item
      self.current += 1
    else:
      self.queue.add_to_tail(item)
      self.storage[self.current] = item
      self.current += 1
    print("list", self.current)


  def get(self):
    return [item for item in self.storage if item is not None]