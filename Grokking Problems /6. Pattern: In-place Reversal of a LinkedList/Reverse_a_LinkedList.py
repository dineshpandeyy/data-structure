'''
Problem Statement #
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
'''
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=' ')
      temp = temp.next
    print()


def reverseLinkedList(head):

    if not head:
        return 
    
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of the original LinkedList are: ", end= "")
  head.print_list()
  result = reverseLinkedList(head)
  print("Nodes of the reversed LinkedList are: ", end= "")
  result.print_list()


main()



