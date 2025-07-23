"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyNode = {None : None}
        cur = head
        while cur:
            copyNode[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copyNode[cur].random =  copyNode[cur.random]
            copyNode[cur].next = copyNode[cur.next]
            cur = cur.next

        return copyNode[head]
