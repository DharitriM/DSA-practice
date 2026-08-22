# Linked List Practice
# Easy

# 1. Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# node1 = Node(10)
# node2 = Node(20)

# node1.next = node2
#  10 -> 20 -> None


# Create a custom linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Append or insert at end
    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode


# Traverse the Linked List (print the Linked List)
    def printLinkedList(self):
        current = self.head

        if current is None:
            print("No nodes present")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# RESULT
ll = LinkedList() # custom linkedlist
ll.printLinkedList()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
print("after insert at end")
ll.printLinkedList()