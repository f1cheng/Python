
import sys
print 'version:{}'.format(sys.version_info)

#lambda
print 'lambda{}begin'.format('='*50)
class lambda_func:
  init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  def __init__(self):
      pass

  @property
  def double(self) :
      print('\ndouble:')
      return lambda x: x*2 

  def filter(self, list=None):
      print('\nfilter:')
      return filter(lambda x: (x%2 == 0), (self.init_list if list is None else list))

  def map(self, list=None):
      print('\nmap:')
      return map(lambda x : x*3, self.init_list if list is None else list)

lam = lambda_func()
#print lam.double()(9)
print lam.double(9)
print lam.filter()
print lam.filter([2 ,2 , 2])
print lam.map()
print lam.map([1, 2, 3])
print 'lambda{}end'.format('='*50)




