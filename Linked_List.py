class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class Linked_List:
  def __init__(self):
    self.head = None

  def add_node(self,x):
    new_node = Node(x)
    if self.head == None:
      self.head = new_node
      return

    node = self.head
    while node.next != None:
      node = node.next
    node.next = new_node

  def add_new_head(self,x):
    new_node = Node(x)
    new_node.next = self.head
    self.head = new_node

  def delete_node(self,node_value):

    if self.head.next == None or not self.head:
      return

    current_node = self.head
    while current_node.next:
      if current_node.next.value == node_value:
        current_node.next = current_node.next.next
      current_node = current_node.next


  def delete_head(self):
    if self.head.next != None:
      self.head = self.head.next

  def print_Linked_list(self):
    current_node = self.head
    while current_node:
      print(current_node.value, end=" --> ")
      current_node = current_node.next
    print("None")

  def Linked_list_tests(self):
    l = Linked_List()

    assert l.head == None, f"Linked list must be empty"

    l.add_node(1) # [1] --> None
    l.add_node(2) # [1] --> [2] --> None
    l.add_node(3) # [1] --> [2] --> [3] --> None
    l.add_node(4) # [1] --> [2] --> [3] --> [4] --> None

    assert l.head.value == 1, f"Head must be 1"

    l.add_new_head("chicken")

    assert l.head.value == "chicken", f"Head expected chicken"

    l.delete_head()
    assert l.head.value == 1, f"Expected 1"

    l.delete_node("4")
    l.delete_node("3")
    assert l.head.next.value == 2, f"Expected 2"

    print("All test passed")



l = Linked_List()
l.Linked_list_tests()
