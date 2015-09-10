class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.head = None
        self.end = None

    def get(self, key):
        """
        :rtype: int
        """
        # print "get",key
        if key in self.d:
            n = self.d[key]
            self.remove(n)
            self.setHead(n)
            return n.val
        else:
            return -1
    def remove(self,n):
        if n.prev == None and n.next != None:
            self.end = n.next
            n.next.prev = None
        elif n.next == None and n.prev != None:
            self.head = n.prev
            n.prev.next = None
        elif n.prev == None and n.next == None:
            self.head = None
            self.end =  None
        else:
            n.next.prev = n.prev
            n.prev.next = n.next
    def setHead(self,n):
        # print "set",n.key
        n.next = None
        n.prev = self.head
        if self.head != None:
            self.head.next = n

        self.head = n
        if self.end == None:
            self.end = self.head
        # print "sethead",self.head.key,self.end.key
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:
            old = self.d[key]
            old.val = value
            # print old.val
            self.remove(old)
            self.setHead(old)
        else:
            created = Node(key,value)
            if len(self.d) < self.capacity:
                self.setHead(created)
            else:
                del self.d[self.end.key]
                self.remove(self.end)
                self.setHead(created)
            self.d[key] = created
        # for key in self.d:
        #     print key,self.d[key].val
        # print "#######"
lruc = LRUCache(2)
lruc.set(2,1)
lruc.set(1,1)
print lruc.get(2)
lruc.set(4,1)
print lruc.get(1)
print lruc.get(2)




        