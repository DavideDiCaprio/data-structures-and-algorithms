class List_Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next: List_Node = None
    
    def get_Node(self, key: int) -> 'List_Node':
        curr = self
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None
        
    def put_Node(self, key: int, val: int) -> None:
        new_node = List_Node(key, val)
        if self.next is None:
            self.next = new_node
            return
            
        new_node.next = self.next
        self.next = new_node
        
    def delete_Node(self, key: int) -> 'List_Node':
        if not self:
            return
        if self.key == key:
            return self.next
        
        current = self
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return self
            current = current.next
        return self

class Hash_Map:
    def __init__(self):
        self.size = 10 
        self.buckets = [None] * self.size
        self.load_factor = 0.75  
        self.item = 0 

    def __getIndex(self, key):
        return key % self.size
    
    def __resize(self):
        new_size = self.size * 2
        new_buckets = [None] * new_size

        for i in range(self.size):
            current = self.buckets[i]
            while current:
                new_index = current.key % new_size
                if new_buckets[new_index] is None:
                    new_buckets[new_index] = List_Node(current.key, current.val)
                else:
                    node = List_Node(current.key, current.val)
                    node.next = new_buckets[new_index]
                    new_buckets[new_index] = node
                current = current.next

        self.buckets = new_buckets
        self.size = new_size

    def put(self, key: int, value: int) -> None:
        index = self.__getIndex(key)
        
        if self.buckets[index] is None:
            self.buckets[index] = List_Node(key, value)
        else:
            node = self.buckets[index].get_Node(key)
            if node:
                node.val = value
            else:
                self.buckets[index].put_Node(key, value)
        
        self.item += 1  
        
        if self.item > self.size * self.load_factor:
            self.__resize()

    def get(self, key: int) -> int:
        index = self.__getIndex(key)
        current = self.buckets[index]

        if current is None:
            return -1  
        node = current.get_Node(key)
        return node.val if node else -1 

    def remove(self, key: int) -> None:
        index = self.__getIndex(key)
        current = self.buckets[index]

        if current is None:
            return  

        if current.key == key:
            self.buckets[index] = current.next  
        else:
            current.delete_Node(key)

        self.item -= 1 
