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
  
  #is_stack_empty test.

  #Check if Stack is succesfuly created.
  assert s != None, f'''The instance is not created successfully'''
  
  #Check if is_stack_empty works.
  s.is_stack_empty()
  assert s == False or s==True, f'Is_stack_empty must return True or False'

  #push test.
  s.push(x=4)

  #Check if push takes an integer.
  if not isinstance(x, int):
    raise ValueError(f'x must be int.')

  print('all tests passed')
