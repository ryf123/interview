# Definition for a undirected graph node
class UndirectedGraphNode(object):
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution(object):
	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		"""
		d = {}
		stack = []
		processed = {}
		stack.append(node)
		head = None
		while stack:
			node = stack.pop(0)
			if node == None:
				return None
			if node.label in processed:
				continue
			processed[node.label] = True
			if node.label not in d:
				newnode = UndirectedGraphNode(node.label)
				d[node.label] = newnode
				head = newnode if head == None else head
			else:
				newnode = d[node.label]
			for neighbor in node.neighbors:
				newneighbor = d[neighbor.label] if neighbor.label in d else UndirectedGraphNode(neighbor.label)
				d[neighbor.label] = newneighbor
				newnode.neighbors.append(newneighbor)
				stack.append(neighbor)
		return head



