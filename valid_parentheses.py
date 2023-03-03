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

def are_parentheses_valid(s):
  pass


def test_are_parentheses_valid():
  
  assert are_parentheses_valid(s='()') != None, f'Function not created succesfuly.'

  try:
    are_parentheses_valid(s='(')
  except RuntimeError:
    pass # give only open parenthesis

  try:
    are_parentheses_valid(s=')')
  except RuntimeError:
    pass # give only closing parenthesis
  
  try:
    are_parentheses_valid(s='()'
  except RuntimeError:
    pass # unexpected error,'()' is a valid input.

  try:
    are_parentheses_valid(s='))((')
  except RuntimeError:
    pass # unmached parentheses
    
  print('All Tests Passed!')

test_are_parentheses_valid()
