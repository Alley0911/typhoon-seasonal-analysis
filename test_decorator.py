import time


def ct(func):
	def inner(*args):
		st = time.time()
		func(*args)
		et = time.time()
		print(et - st)
	return inner

@ct
def function(a):
	time.sleep(1)
	print(a)

function(3)

class test(object):
	a = 1
	def __init__(self):
		print(self.a)
a = test()