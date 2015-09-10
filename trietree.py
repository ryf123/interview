class TrieNode(object):
	def __init__(self,val):
		"""
		Initialize your data structure here.
		"""
		self.val = val
		self.child = []
		self.termintate = False
class Trie(object):

	def __init__(self):
		self.root = TrieNode("")
		

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		found = False
		current = self.root
		for w in word:
			found = False
			for child in current.child:
				if w == child.val:
					current = child
					found = True
			if not found:
				node = TrieNode(w)
				current.child.append(node)
				current = node
		current.termintate = True
	def search(self, word,startnode = None):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		stack = 0
		match = 0
		if startnode:
			current = startnode
		else:
			current = self.root
		for i,w in enumerate(word):
			found = False
			if w == ".":
				for child in current.child:
					if i+1 == len(word) and child.termintate:
						return True
					if self.search(word[i+1:],startnode=child):
						return True
				return False
			for child in current.child:
				if w == child.val:
					match +=1
					found = True
					current = child
					continue
			if not found:
				return False
			if match == len(word):
				return True if current.termintate else False
		return False
	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie
		that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		
		current = self.root
		for w in prefix:
			found = False
			for child in current.child:
				if w == child.val:
					found = True
					current = child
					continue
			if not found:
				return False
				
		return True 

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("abc")
trie.insert("abcd")
trie.insert("abcde")
print trie.search(".")