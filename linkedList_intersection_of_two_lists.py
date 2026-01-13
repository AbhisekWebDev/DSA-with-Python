# Question:
# Given the heads of two singly linked-lists headA and headB, 
# return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, 
# return null.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :

        p1 = headA
        p2 = headB

        count = 0

        while True :

            # yahi intersection point h
            if p1 == p2 :
                return p1

            p1 = p1.next
            p2 = p2.next

            if p2 == None :
                count += 1
                p2 = headA
            
            if p1 == None :
                p1 = headB
            
            if count > 1 :
                return None
            
# Helper: build linked list
def build_list(arr):
    head = None
    curr = None
    for val in arr:
        if not head:
            head = ListNode(val)
            curr = head
        else:
            curr.next = ListNode(val)
            curr = curr.next
    return head


# Helper: print linked list
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Create common part
common = ListNode(7)
common.next = ListNode(8)

# List A
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = common

# List B
headB = ListNode(4)
headB.next = ListNode(5)
headB.next.next = common

sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)

print("Intersection Node Value:", intersection.val if intersection else None)


# List A
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)

# List B
headB = ListNode(4)
headB.next = ListNode(5)

sol = Solution()
intersection = sol.getIntersectionNode(headA, headB)

print("Intersection Node Value:", intersection.val if intersection else None)