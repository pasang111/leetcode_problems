# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()  # Starting node for the merged list
        current = dummy  # Keeps track of where to add the next node

        while list1 and list2:  # Keep going until one list is empty
            if list1.val <= list2.val:  # Pick the smaller value
                current.next = list1  # Add the node from list1
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Add the node from list2
                list2 = list2.next  # Move to the next node in list2

            current = current.next  # Move to the last added node

        # Attach whatever is left in either list
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next  # Return the head of the merged list
