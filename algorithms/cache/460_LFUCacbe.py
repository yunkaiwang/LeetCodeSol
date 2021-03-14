class ListNode:  # doubly linked list
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LFUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.linkedListMap = {}
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1

        if key in self.map:
            (node, freq) = self.map[key]
            (head, tail) = self.linkedListMap[freq]

            if node == tail:
                tail = node.prev
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                head = node.next

            # node is the last element in the linked list with frequency freq
            if head == None and tail == None:
                del self.linkedListMap[freq]
            else:
                self.linkedListMap[freq] = (head, tail)

            node.prev = None
            node.next = None

            if freq + 1 not in self.linkedListMap:
                self.linkedListMap[freq + 1] = (node, node)
            else:
                (head, tail) = self.linkedListMap[freq + 1]
                head.prev = node
                node.next = head
                self.linkedListMap[freq + 1] = (node, tail)

            self.map[key] = (node, freq + 1)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.map:
            (node, freq) = self.map[key]
            (head, tail) = self.linkedListMap[freq]
            node.val = value

            if node == tail:
                tail = node.prev
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                head = node.next

            # node is the last element in the linked list with frequency freq
            if head == None and tail == None:
                del self.linkedListMap[freq]
            else:
                self.linkedListMap[freq] = (head, tail)

            node.prev = None
            node.next = None

            if freq + 1 not in self.linkedListMap:
                self.linkedListMap[freq + 1] = (node, node)
            else:
                (head, tail) = self.linkedListMap[freq + 1]
                head.prev = node
                node.next = head
                self.linkedListMap[freq + 1] = (node, tail)
            self.map[key] = (node, freq + 1)
            return

        if self.size >= self.capacity:
            least_freq = min(self.linkedListMap.keys())
            (head, tail) = self.linkedListMap[least_freq]
            del self.map[tail.key]
            if head == tail:
                del self.linkedListMap[least_freq]
            else:
                tail.prev.next = None
                self.linkedListMap[least_freq] = (head, tail.prev)
            self.size -= 1

        node = ListNode(key, value)
        self.map[key] = (node, 1)

        if 1 in self.linkedListMap:
            (head, tail) = self.linkedListMap[1]
            head.prev = node
            node.next = head
            self.linkedListMap[1] = (node, tail)
        else:
            self.linkedListMap[1] = (node, node)
        self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)