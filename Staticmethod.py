from typing import Callable


class Staticmethod:
    def __init__(self, decorated_method: Callable):
        """Initialize the Staticmethod decorator.
        
        Args:
            decorated_method (Callable): The method to be decorated as static.
        """
        self.decorated_method = decorated_method
        
    def __get__(self, instance, owner):
        """Retrieve the static method without binding it to an instance.
        
        Args:
            instance: The instance that the method is accessed through.
            owner: The owner class of the instance.
            
        Returns:
            The original method that was decorated as static.
        """
        return self.decorated_method
