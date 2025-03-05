from utility import ListNode, print_list, create_linked_list


def reverseList(head: ListNode | None) -> ListNode | None:
    """
    Reverse a linked list.
    
    Args:
        head: The head of the linked list to reverse
        
    Returns:
        The head of the reversed linked list
    """
    curr = head
    res = None

    while curr:
        next_node = curr.next
        curr.next = res
        res = curr
        curr = next_node
    return res


def main():
    """Create example linked lists and demonstrate list reversal."""
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    
    # Print original list
    print("Original linked list:")
    print_list(head)
    
    # Reverse the list
    reversed_head = reverseList(head)
    
    # Print reversed list
    print("Reversed linked list:")
    print_list(reversed_head)


if __name__ == "__main__":
    main()