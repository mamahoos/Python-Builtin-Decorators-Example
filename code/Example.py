from Property import Property
from Classmethod import Classmethod
from Staticmethod import Staticmethod


class Example:
    def __init__(self, value):
        self._value = value

    @Property
    def value(self):
        """Property decorator example: Get the value."""
        print('- Getting value -')
        return self._value

    @value.setter
    def value(self, new_value):
        """Property decorator example: Set the value."""
        print('- Setting value -')
        self._value = new_value

    @value.deleter
    def value(self):
        """Property decorator example: Delete the value."""
        print('- Deleting value -')
        del self._value

    @Classmethod
    def from_string(cls, string_value):
        """Classmethod decorator example: Create an instance from a string."""
        value = int(string_value)
        return cls(value)

    @Staticmethod
    def is_integer(value):
        """Staticmethod decorator example: Check if a value is an integer."""
        return isinstance(value, int)

# Create an instance using the classmethod
example_from_string = Example.from_string("10")

# Access and modify the property
print(f"Initial value: {example_from_string.value}")
example_from_string.value = 20
print(f"New value: {example_from_string.value}")
del example_from_string.value

# Use the staticmethod
print(f"Is 5 an integer? {Example.is_integer(5)}")
print(f"Is 'hello' an integer? {Example.is_integer('hello')}")