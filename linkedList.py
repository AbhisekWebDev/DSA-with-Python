# Define Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse Linked List
def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next     # store next
        curr.next = prev    # reverse link
        prev = curr         # move prev
        curr = nxt          # move forward
    
    return prev

# Helper function to print list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    
    return head

head = create_linked_list([1, 2, 3, 4])

print("Original List:")
printList(head)

# Call reverse
reversed_head = reverseList(head)

print("Reversed List:")
printList(reversed_head)

# Point the head node to the new reversed head :-: reset the head node
head = reversed_head

# Insertion operation at beginning of linked list
def insert_at_beginning(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

print("\nAfter Inserting at Beginning (0):")
head = insert_at_beginning(head, 0)
printList(head)

# Insertion operation at end of linked list
def insert_at_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    
    curr = head
    while curr.next:
        curr = curr.next
    
    curr.next = new_node
    return head

print("\nAfter Inserting at End (5):")
head = insert_at_end(head, 5)
printList(head)

# Insertion at specific position
def insert_at_position(head, val, pos):
    new_node = ListNode(val)
    if pos == 0:
        new_node.next = head
        return new_node
    
    curr = head
    for _ in range(pos - 1):
        if not curr:
            break
        curr = curr.next
    
    if curr:
        new_node.next = curr.next
        curr.next = new_node
    
    return head

print("\nAfter Inserting 9 at Position 2:")
head = insert_at_position(head, 9, 2)
printList(head)

# Delete a node from beginning of linked list
def delete_from_beginning(head):
    if not head:
        return None
    
    return head.next

print("\nAfter Deleting from Beginning:")
head = delete_from_beginning(head)
printList(head)

# Delete a node from end of linked list
def delete_from_end(head):
    if not head:
        return None
    
    if not head.next:
        return None
    
    curr = head
    while curr.next and curr.next.next:
        curr = curr.next
    
    curr.next = None
    return head

print("\nAfter Deleting from End:")
head = delete_from_end(head)
printList(head)

# Delete a node from specific position
def delete_from_position(head, pos):
    if not head:
        return None
    
    if pos == 0:
        return head.next
    
    curr = head
    for _ in range(pos - 1):
        if not curr.next:
            return head
        curr = curr.next
    
    if curr.next:
        curr.next = curr.next.next
    
    return head

print("\nAfter Deleting from Position 2:")
head = delete_from_position(head, 2)
printList(head)

# Used in:

# Implementing Stacks and Queues

# Manipulating Data Sequences

# Memory Management