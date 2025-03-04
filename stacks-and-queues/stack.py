class Stack():

  def __init__(self):
    self.stack = []

  def is_stack_empty(self):
    return len(self.stack) == 0
  
  def push(self, x):
    self.stack.append(x)

  def pop(self):
    if self.is_stack_empty():
      raise RuntimeError()
    return self.stack.pop()

  
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
  assert s_pop_element == 'letter', f'''Unespected output, get: {s_pop_element}, expected 'letter'. '''
  s_pop_element = s.pop() 
  assert s_pop_element == 4, f'''Unespected output, get: {s_pop_element}, expected '4'. '''

  assert s.is_stack_empty() == True, f'At this point stack must be empty.'

  try:
    s.pop() 
  except RuntimeError:
    pass #Pop must not possible, stack must be empty.

  print('all tests passed')
