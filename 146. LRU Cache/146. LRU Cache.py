class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hash_dict = {}

    def insert_at_beginning(self, node):
        ptr = self.head.next
        ptr.prev = node
        node.next = ptr
        self.head.next = node
        node.prev = self.head

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def last_accessed(self, node):
        self.delete_node(node)
        self.insert_at_beginning(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_dict:
            loc = self.hash_dict[key]
            self.last_accessed(loc)
            return loc.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash_dict:
            old_node = self.hash_dict[key]
            self.delete_node(old_node)

        new_node = ListNode(key, value)
        self.insert_at_beginning(new_node)
        self.hash_dict[key] = new_node

        if len(self.hash_dict) > self.capacity:
            node_to_del = self.tail.prev
            self.delete_node(node_to_del)
            del self.hash_dict[node_to_del.key]

    def print_list(self):
        ptr = self.head
        while ptr:
            print (ptr.key)
            ptr = ptr.next
    def print_forward(self):
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.key) + "--> "
            itr = itr.next
        print(llstr)

    def print_backward(self):
        llstr = ""
        itr = self.tail
        while itr:
            llstr += str(itr.key) + "--> "
            itr = itr.prev
        print(llstr)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)