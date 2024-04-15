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


#-------#


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @Property
    def age(self):
        "The person's age"
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0 < value < 120:
            self._age = value
        else:
            raise ValueError("Age must be an integer between 1 and 119")
        

mamahoos = Person('mamahoos', 17)

mamahoos.age += 1		# ^_^

print(
    mamahoos.age
)