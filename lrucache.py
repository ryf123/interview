# double link list so that delete complexity is O(1)
# dict is used to store point to quickly get value
class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):

    head = Node(100,100)
    end = Node(-1,-1)
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.head.prev = self.end
        self.end.next = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.d:
            n = self.d[key]
            self.remove(n)
            self.setHead(n)
            return n.val
        else:
            return -1
    def remove(self,n):
        n.next.prev = n.prev
        n.prev.next = n.next

        
    def setHead(self,n):
        n.prev = self.head.prev
        n.prev.next = n
        self.head.prev = n
        n.next = self.head

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:
            old = self.d[key]
            old.val = value
            self.remove(old)
            self.setHead(old)
        else:
            created = Node(key,value)
            if len(self.d) < self.capacity:
                pass
            else:
                del self.d[self.end.next.key]
                self.remove(self.end.next)
            self.setHead(created)
            self.d[key] = created
lruc = LRUCache(2)
lruc.set(2,2)
lruc.set(1,1)
print lruc.get(2)
lruc.set(4,1)
print lruc.get(1)
print lruc.get(2)




        