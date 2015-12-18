class Process:
	def __init__(self,at,et):
		self.at = at
		self.et = et
class RoundandRobin:

	def start(self,ats,ets,q):
		assert(len(ats) == len(ets))
		l = len(ats)
		if l == 0:
			return 0
		i = 0
		queue = []
		currentTime = 0
		waitTime = 0
		while queue or i<l:
			if len(queue) == 0:
				queue.append(Process(ats[i],ets[i]))
				currentTime = ats[i]
				i+=1
			else:
				currentprocess = queue.pop(0)
				waitTime += currentTime - currentprocess.at
				currentTime += min(q,currentprocess.et)
				while i < l and ats[i] <= currentTime:
					queue.append(Process(ats[i],ets[i]))
					i+=1
				if currentprocess.et > q:
					queue.append(Process(currentTime,currentprocess.et-q))
		return waitTime*1.0/l
rr  = RoundandRobin()
print rr.start([0,1,4],[5,2,3],3)
print rr.start([1,1,4],[2,2,2],1)
assert(rr.start([1],[1],3) == 0) 
assert(rr.start([],[],3) == 0) 
assert(rr.start([1,2],[1,2],1) == 0)

