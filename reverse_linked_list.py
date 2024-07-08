# Reverse a Linked List

# Easy

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# In O(n) time and O(1) memory

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        return previous
    


# Recursive, O(n) time and O(n) memory

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(current, previous):
            if not current:
                return previous
        
            next = current.next
            current.next = previous
            return reverse(next, current)
        return reverse(head, None)
        