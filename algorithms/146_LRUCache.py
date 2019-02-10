class ListNode: # doubly linked list
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    idea is to use a doubly linked list to store the access priority of the elements, and use a hashmap to keep track of whether we have the key or not(beats 80% on Leetcode)
    """
    def __init__(self, capacity: 'int'):
        self.size = capacity
        self.head = None
        self.tail = None
        self.dict = {}
        self.cur_size = 0

    def get(self, key: 'int') -> 'int':
        if key in self.dict:
            node = self.dict[key]
            
            if node.prev:
                if node == self.tail:
                    self.tail = node.prev
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                node.next = self.head
                self.head.prev = node
                self.head = node
                node.prev = None
            
            return node.val
        
        return -1

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.dict:
            node = self.dict[key]
            if node.prev:
                if node == self.tail:
                    self.tail = node.prev
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                node.next = self.head
                self.head.prev = node
                self.head = node
                node.prev = None
            node.val = value
            return
            
        if self.cur_size == self.size:
            last_node = self.tail
            self.tail = last_node.prev
            last_node_key = last_node.key
            del self.dict[last_node_key]
            self.cur_size -= 1
        
        node = ListNode(key, value)
        self.dict[key] = node
        node.next = self.head
        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.cur_size += 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)