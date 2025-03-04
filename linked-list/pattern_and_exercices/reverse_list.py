class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    res = None

    while curr:
        next_node = curr.next
        curr.next = res
        res = curr
        curr = next_node
    return res
            