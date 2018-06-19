import threading
import time

lock = threading.Lock()

def f(r):
	global lock
	time.sleep(0.0008)
	lock.acquire(True)
	print "This is running in thread {}".format(r.n)
	lock.release()
	r.r = r.n *  2
	
class R(object):
	def __init__(self, n):
		self.n = n
	
	
r0 = R(0)
r1 = R(1)
r2 = R(2)
r3 = R(3)
	
t0 = threading.Thread(target=f, args=(r0,))
t1 = threading.Thread(target=f, args=(r1,))
t2 = threading.Thread(target=f, args=(r2,))
t3 = threading.Thread(target=f, args=(r3,))

t0.start()
t1.start()
t2.start()
t3.start()
lock.acquire(True)
print "We started the threads"
lock.release()
t0.join()
t1.join()
t2.join()
t3.join()

print r0.r, r1.r, r2.r, r3.r


