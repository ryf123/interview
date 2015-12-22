class WindowSum:
	def solve(self,array,windowSize):
		ret = [] 
		value = 0
		stack = []
		for i,ele in enumerate(array):
			stack.append(ele)
			if i<windowSize-1:
				continue
			elif i==windowSize-1:
				total = sum(stack)
				ret.append(total)
			else:
				last = stack.pop(0)
				total = total-last+ele
				ret.append(total)
		return ret
w = WindowSum()
print w.solve([4,2,73,11,-5],2)
print w.solve([4,2,73,11,-5],3)

