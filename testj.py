class Solution(object):
	def generate_row(self,stack,maxWidth,length,left_align=False):			
		spaces = maxWidth - length
		if left_align or len(stack) == 1:
			spaces = spaces - len(stack) +1
			trailing_space = ""
			while spaces:
				trailing_space += " "
				spaces -=1
			return " ".join(stack) + trailing_space
		l = len(stack)
		while spaces:
			i = 0
			while i<l-1 and spaces:
				stack[i] += " "
				spaces -=1
				i+=1
		return "".join(stack)

	def fullJustify(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""
		ret = []
		stack = []
		length = 0
		l = len(words)
		i = 0
		if maxWidth == 0:
			if "".join(words) == "":
				return [""]
			else:
				return []
		while i<l:
			word  = words[i]
			if length + len(word) + (len(stack)-1) +1 <= maxWidth:
				length += len(word)
				stack.append(word)
				i+=1
			elif length + len(word) + (len(stack)-1) +1 > maxWidth:
				ret.append(self.generate_row(stack,maxWidth,length))
				length = 0
				stack = []
		if len(stack)>0:
			ret.append(self.generate_row(stack,maxWidth,length,left_align=True))
		return ret
s = Solution()
print s.fullJustify(["Listen","to","many,","speak","to","a","few."],6)
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)

