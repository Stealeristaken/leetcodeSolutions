# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import ListNode
class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val, node.next = node.next.val, node.next.next