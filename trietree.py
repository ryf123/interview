class TrieNode:
	def __init__(self,val=""):
	# Initialize your data structure here.
		self.val = val
		self.child = {}
		self.isEnd = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
	def addWord(self, word):
		l = len(word)
		i = 0
		current = self.root
		while i<l:
			if word[i] in current.child:
				current = current.child[word[i]]
			else:
				newNode = TrieNode(word[i])
				current.child[word[i]] = newNode
				current = newNode
			i+=1
		current.isEnd = True 
  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
	def search(self, word,current = None):
		if current == None:
			current = self.root
		l = len(word)
		i = 0
		while i<l:
			if word[i] in current.child:
				current = current.child[word[i]]
			else:
				if word[i] == ".":
					for key in current.child:
						if self.search(word[i+1:],current=current.child[key]):
							return True
				return False
			i+=1
		return current.isEnd


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.addWord("abc")
trie.addWord("abcd")
trie.addWord("abcde")
print trie.search("abce.")