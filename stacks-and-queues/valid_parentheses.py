'''
In this exercise you are going to implement the function are_parentheses_valid(s)
which takes as input a string that contains any combination of the following two
chatacters: '(', ')' and returns True if the parentheses are valid, False otherwise.

Note: assume there are NO other characters than '(', ')' in the input string.

A string of parentheses s, is valid if and only if, for each open parentheses '(',
there is a corresponding closing parentheses ')', and vice versa. If a closing
parenthesis is unmatched by an opening one, or an opening one is not matched by a
closing parentheses, then the string is not valid.

Examples:
'()' -> valid
'(' -> not valid
'(()' -> not valid
'(())' -> valid
'((())())' -> valid
'((())()))' -> not valid.

To solve this exercise, start by implementing the test function. Once you are
satisfied with the test, move on to the implementation of the main function.
'''

from Stack import Stack 

def are_parentheses_valid(s):
  stack = Stack()
  for p in s:
    if p == '(':
      stack.push(p)
    else:
      if p == ')':
        if stack.is_stack_empty():
          return False
        stack.pop()
  if stack.is_stack_empty():
    return True
  return False
  
  
def test_are_parentheses_valid():
  
  assert are_parentheses_valid(s='()') == True, f''' '()' is a valid input. Function must return True. '''
  assert are_parentheses_valid(s='(') == False, f''' '(' isn't a valid input. A open parentheses require a closed one. '''
  assert are_parentheses_valid(s=')') == False, f''' ')' isn't a valid input. A closed parentheses require a open one. '''
  assert are_parentheses_valid(s='(()))') == False, f''' '(()))' isn't a valid input. Number of open and closed parentheses is not the same. '''
  assert are_parentheses_valid(s='))((') == False, f'''If a closed parentheses appears before open one is impossibile to satisfy function requirement. '''
  assert are_parentheses_valid(s='(()))()') == False, f''' '(()))()' isn't a valid input. Unmached parentheses. '''
  assert are_parentheses_valid(s='((())())(())') == True, f''' For each open parentheses there is a closed one. Function must return True. '''

  print('All Tests Passed!')

test_are_parentheses_valid()
