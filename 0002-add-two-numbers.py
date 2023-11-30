from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        carry = 0

        output_node = ListNode()
        current_node = output_node

        while True:
            # Sum the integers and carry an integer over
            val = (
                (n1.val if n1 is not None else 0)
                + (n2.val if n2 is not None else 0)
                + carry
            )
            if val > 9:
                carry = val // 10
                val = val % 10
            else:
                carry = 0

            # Add sum to output node
            current_node.val = val

            # Progress to the next node
            n1 = n1.next if n1 is not None else None
            n2 = n2.next if n2 is not None else None

            if n1 is not None or n2 is not None or carry != 0:
                current_node.next = ListNode()
                current_node = current_node.next
            else:
                return output_node
