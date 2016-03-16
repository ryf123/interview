# wordpossibility = float(26)/27
# ret = []
# for x in range(1,100):
# 	ans = 1
# 	for i in xrange(x):
# 		ans *=wordpossibility
# 	ret.append((x,round((ans*float(1)/27),2))) 
# print ret
the = 6
threshold = 40
total = 1
count = 1
while total < threshold:
	total += float(the)/count
	count+=1
print count