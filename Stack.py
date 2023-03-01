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
  #Create stack.
  s = Stack()
  
  #Check if Stack is succesfuly created.
  assert s != None, f'The instance is not created successfully.'

  #Ckeck if s is empty.
  assert s.is_stack_empty(), f'At this point stack must be empty.'

  s.push(x=4)
  s.push(x='letter') 

  assert s.is_stack_empty() == False, f' Stack must not be empty at this point. '
  
  #Check if pop remove items correctly.
  s_pop_element = s.pop() 
  assert s_pop == 'letter', f'Unespected output. '
  s_pop_element = s.pop() 
  assert s_pop == '4', f'Unespected output. '

  assert s.is_stack_empty() == True, f'At this point stack must be empty.'

  try:
    s.pop() 
    assert s.is_stack_empty == True, f'Pop must not possible, stack must be empty.'
  except RuntimeError:
    pass # 

  print('all tests passed')
