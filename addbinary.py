class Solution(object):
	def addBinary(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		a = a[::-1]
		b = b[::-1]
		la = len(a)
		lb= len(b)
		l = max(la,lb)
		i = 0
		addon = 0
		total = ""
		while i < l:
			if i <la:
				aa = int(a[i])
			else:
				aa = 0
			if i < lb:
				ba = int(b[i])
			else:
				ba = 0
			# print i,total,addon,[aa,ba],la,lb
			s = aa + ba +addon
			if s == 3:
				addon = 1
				total +="1"
			elif s==2:
				total +="0"
				addon = 1
			elif s == 1:
				total+= "1"
				addon = 0
			else:
				total += "0"
				addon = 0

			i +=1
		total += "" if addon ==0 else "1"
		return total[::-1]
s = Solution()
a = "11"
b = ""
print s.addBinary(a,b)