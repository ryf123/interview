class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def findSubstring(self, s, words):
		ret = []
		nw = len(words)
		#words = sorted(words) #sort the word
		#words = "".join(words) # concatenate words into a long string
		if nw == 0:
			return ret
		wl = len(words[0])
		csl = wl *nw
		sl = len(s)
		if(sl < csl):
			return ret
		i = 0
		worddict ={}
		for word in words:
			if word in worddict:
				worddict[word] +=1
			else:
				worddict[word] =1
		print worddict
		while( i < sl - csl+1): 
			# break the string into equal length of words and compare with words
			temparray = []
			tempworddict = {}
			for j in range(0,nw):
				word = s[j*wl+i:i+wl*(j+1)]
				if word in tempworddict:
					tempworddict[word] +=1
				else:
					tempworddict[word] =1 
			match = True
			for word in words:
				if word in tempworddict:
					if worddict[word] != tempworddict[word]:
						match = False
						break
				else:
					match = False
					break
			if match:
				ret.append(i)
			i+=1		
		return ret
sl = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
print sl.findSubstring(s,words)