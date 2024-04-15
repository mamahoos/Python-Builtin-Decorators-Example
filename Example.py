from Property import Property


class foo:
	def __init__(self, value):
		self.__value = value
			
	def getter(self):
		print('Getting value')
		return self.__value
			
	def setter(self, value):
		print('Setting value to ' + value)
		self.__value = value

	def deleter(self):
		print('Deleting value')
		del self.__value

	value = Property(getter, setter, deleter, )
	

x = foo('meow')
print(x.value)
	
x.value = 'meow again'
print(x.value)

del x.value
try:    print(x.value)     
except AttributeError as e:     print("AttributeError!")
	
