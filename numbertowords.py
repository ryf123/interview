class Solution(object):
	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num == 0:
			return "Zero"
		ret = ""
		less20words = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
		tenswords = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
		largewords = ["Thousand", "Million", "Billion"]
		def lessthan20(num):
			# print num
			return " " + less20words[num]
		def tens(num):
			if num < 20:
				ret = lessthan20(num)
			else:
				ret = " " + tenswords[num/10]
				# print num

				ret += lessthan20(num%10)
			return ret.rstrip()
		def hundred(num):
			ret = ""
			if num >= 100:
				ret += lessthan20(num/100) + " Hundred"
			# else:
			ret += tens(num % 100)
			return ret.rstrip()
		def thousand(num):
			ret = ""
			if num >= 1000:
				ret += hundred(num/1000) + " Thousand"
			ret += hundred(num%1000)
			return ret.rstrip()
		def million(num):
			ret = ""
			if num >= 1000*1000:
				ret += hundred(num/(1000*1000)) + " Million"
			ret += thousand(num%(1000*1000))
			return ret.rstrip()
		def billion(num):
			ret = ""
			if num >= 1000*1000*1000:
				ret = hundred(num/(1000*1000*1000)) + " Billion"
			ret += million(num%(1000*1000*1000))
			return ret.rstrip()

		if num<20:
			ret = lessthan20(num)
		elif num<100:
			ret = tens(num)
		elif num <1000:
			ret = hundred(num)
		elif num< 1000*1000:
			ret = thousand(num)
		elif num < 1000*1000*1000:
			ret = million(num)
		else:
			ret = billion(num)
		ret =  ret.lstrip()
		return ret.rstrip()

s = Solution()
tests = [0,1,2,3,10,15,20,99,100,111,1000,1111,111111111,1111111111,50868]
for t in tests:
	print t,s.numberToWords(t)

