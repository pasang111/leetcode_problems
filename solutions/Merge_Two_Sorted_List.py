# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Define a node because Python needs to know how each linked-list node works
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Store the node's value
        self.next = next  # Point to the next node


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()  # Create a starting node for the merged list
        current = dummy  # Keep track of where to add the next node

        # Compare both lists until one becomes empty
        while list1 and list2:
            if list1.val <= list2.val:  # Pick the smaller value
                current.next = list1  # Add the node from list1
                list1 = list1.next  # Move to the next node in list1
            else:
                current.next = list2  # Add the node from list2
                list2 = list2.next  # Move to the next node in list2

            current = current.next  # Move to the node we just added

        # Attach the remaining nodes from either list
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next  # Return the head of the merged list
