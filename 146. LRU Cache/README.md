### 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:  

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.  
int get(int key) Return the value of the key if the key exists, otherwise return -1.  
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.  
The functions get and put must each run in O(1) average time complexity.  

**Example 1:**

**Input**

["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]  
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] 

**Output**  

[null, null, null, 1, null, -1, null, -1, 3, 4]  

**Explanation**

LRUCache lRUCache = new LRUCache(2);  
lRUCache.put(1, 1); // cache is {1=1}  
lRUCache.put(2, 2); // cache is {1=1, 2=2}  
lRUCache.get(1);    // return 1  
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}  
lRUCache.get(2);    // returns -1 (not found)  
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}  
lRUCache.get(1);    // return -1 (not found)  
lRUCache.get(3);    // return 3  
lRUCache.get(4);    // return 4  
 

**Constraints:**

1 <= capacity <= 3000  
0 <= key <= 104  
0 <= value <= 105  
At most 2 * 105 calls will be made to get and put.

```python
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
```