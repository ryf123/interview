import sys
class Sum(object):
	"""docstring for Sum"""
	def add(self,a,b):
		return int(a) + int(b)
def Print(num,result):
	return "Case #{}\n{}\n".format(str(num),str(result))
def saveFile(content,filename="sum_sample_solution_python.out"):
	with open (filename,'w') as f:
		f.write(content)
def main(filename):
	s = Sum()
	o = ""
	with open (filename,'r') as f:
		lines = f.readlines()
		n = lines[0]
		i = 1
		while i <= int(n):
			a,b = lines[i].split(" ")
			o += Print(i,s.add(a,b))
			i += 1
	print o
	saveFile(o)


if __name__ == '__main__':
	main(sys.argv[1])