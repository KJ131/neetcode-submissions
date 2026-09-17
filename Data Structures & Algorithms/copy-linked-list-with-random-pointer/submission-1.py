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
        hash_map = {}
        curr = head
        
    
        def get_or_create_node(node):
            if node is None:
                return None
            if node not in hash_map:
                hash_map[node] = Node(node.val)
            return hash_map[node]
        while curr:
            copy = get_or_create_node(curr)
            copy.next = get_or_create_node(curr.next)
            copy.random = get_or_create_node(curr.random)
            curr = curr.next
        return hash_map.get(head, None) 

        