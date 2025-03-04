class Queue():

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    #Add element to the back, complexity = O(1)
    def enqueue(self, x):
        self.queue.append(x)

    #Remove element from the front, complexity = O(1)
    def dequeue(self):
      if self.is_empty():
        raise RuntimeError()

      return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def print_queue(self):
      print(self.queue)

    def test_queue(self):
      #Create Queue.
      q = Queue()

      #q = []

      #Check if Queue is succesfuly created.
      assert q != None, f'The instance is not created successfully.'

      #Ckeck if s is empty.
      assert q.is_empty(), f'At this point queue must be empty.'

      q.enqueue(1)
      #q = [1]
      q.enqueue(2)
      #q = [1,2]

      assert q.is_empty() == False, f' Queue must not be empty at this point. '

      assert q.size() == 2, f'size 2'
      
      q.enqueue(3)
      #q = [1,2,3]

      assert q.dequeue() == 1, f"Expected '1'"

      #q = [2,3]

      q.dequeue()
      #q = [3]
      q.dequeue()
      #q = []

      try:
        q.dequeue()
      except RuntimeError:
        pass #Pop must not possible, stack must be empty.

      print('all tests passed')
