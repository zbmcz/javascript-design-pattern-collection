#coding=utf-8
# 伪代码实现..
class F1(object):
	def show(self):
		print 'F1 show'

class S1(F1):
	def show(self):
		print 'S1 show'

class S2(F1):
	def show(self):
		print 'S2 show'


def test(obj):
	obj.show()

s1_obj = S1()
test(s1_obj)

s2_obj = S2()
test(s2_obj)

