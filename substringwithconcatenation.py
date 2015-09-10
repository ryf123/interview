class Solution:
	# @param {string} s
	# @param {string[]} words
	# @return {integer[]}
	def findSubstring(self, s, words):
		ret = []
		if len(words) == 0:
			return ret
		wl = len(words[0]) # len of each word, since they are the same lenght
		nw = len(words) # number of words
		csl = nw*wl # concatenated string lenght = #words*wordlenght 
		sl = len(s)
		if(sl < csl):
			return ret
		d = {}
		for word in words:
			if word not in d:
				d[word] = 1
			else:
				d[word] +=1
		
		i = 0
		mark = [0] * sl
		for i,ss in enumerate(s):
			word = s[i:i+wl]
			if word in d:
				mark[i] = 1
		i=0
		while( i < sl - csl+1):
			if not mark[i]:
				i+=1
				continue
			tempdict  = d.copy()
			j = i
			counter = 0 
			while(tempdict):
				substring = s[j: j+wl]
				if substring in tempdict:
					tempdict[substring] -=1
					if tempdict[substring] == 0:
						del tempdict[substring]
					j+=wl
				else:
					j+=1
					break
			if not tempdict:
				ret.append(i)
				i+= 1
			else:
				i+=1
		return ret

sl = Solution()
s ="barfoothefoobarman"
words = ["foo","bar"]
print sl.findSubstring(s,words)