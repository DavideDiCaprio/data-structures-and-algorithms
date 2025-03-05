class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head: ListNode | None) -> None:
    """
    Print a linked list in a readable format.
    
    Args:
        head: The head of the linked list to print
    """
    current = head
    nodes = []
    while current:
        nodes.append(str(current.val))
        current = current.next
    print(" -> ".join(nodes))


def create_linked_list(values: list) -> ListNode | None:
    """
    Create a linked list from a list of values.
    
    Args:
        values: A list of values to convert to a linked list
        
    Returns:
        The head of the created linked list, or None if values is empty
    """
    if not values:
        return None
        
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        
    return head