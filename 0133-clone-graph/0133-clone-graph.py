"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        old_to_new = {} # dfs로 탐색 및 복사하기 때문에 무한루프를 방지하기 위해 visited 역할을 할 dict 필요
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node] # 이미 복사된 노드면 기존 노드 return
            copied = Node(node.val) # 처음 보는 노드면 Node 자료구조 활용 새로운 노드 반환
            old_to_new[node] = copied
            for neighbor in node.neighbors:
                copied.neighbors.append(dfs(neighbor))
            return copied
        return dfs(node)
            