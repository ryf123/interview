import threading
class Thread(threading.Thread):
	def __init__(self, t, *args):
		threading.Thread.__init__(self, target=t, args=args)
		self.start()
count = 0
lock = threading.Lock()
stack = []
def incre(name):
	print name 
	global count 
	lock.acquire()
	try:
		count += 1
		stack.append(count)
	finally:
		lock.release()

def bye():
	for x in xrange(10):
		incre("b")

def hello_there():
	for x in xrange(10):
		incre("h")

def main():
	hello = Thread(hello_there)
	goodbye = Thread(bye)
if __name__ == '__main__':
	main()