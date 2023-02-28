class Stack():

  def __init__(self):
    pass

  def is_stack_empty(self):
    pass

  def push(self, x):
    pass

  def pop(self):
    pass 


def test_stack():
  s = Stack()
  
  #Check if Stack is succesfuly created.
  assert s != None, f'The instance is not created successfully.'

  #Ckeck if is stack is empty.
  s_empty_test = s.is_stack_empty()
  assert s_empty_test == True, f'At this point stack must be empty.'
  
  #Check if push correctly add item in s.
  s.push(x=4)
  s.push(x='letter')
  
  s_push_test = s.is_stack_empty()
  assert s_push_test == False, f'Stack must not be empty at this point. '

  #Check if pop remove items correctly.
  s.pop()
  s.pop()
  
  s_pop_test = s.is_stack_empty()
  assert s_pop_test == True, f'At this point stack must be empty.'
  
  #
  try:
    empty_s = s.pop() 
    assert empty_s == False, f'Pop must not possible, stack must be empty.'
  except RuntimeError:
    pass #
