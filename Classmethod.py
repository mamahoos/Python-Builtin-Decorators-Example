from functools import wraps
from typing import Callable


class Classmethod:
    def __init__(self, decorated_method: Callable):
        """Initialize the Classmethod decorator.
        
        Args:
            decorated_method (Callable): The method to be decorated as a class method.
        """
        self.decorated_method = decorated_method
        
    def __get__(self, instance, owner):
        """Retrieve the class method and bind it to the class (owner).
        
        Args:
            instance: The instance that the method is accessed through. This is ignored for class methods.
            owner: The class that the method is accessed through.
            
        Returns:
            The wrapper function that binds the first argument of the decorated method to the owner class.
        """
        
        @wraps(self.decorated_method)
        def wrapper(*args, **kwargs):
            """Wrap the decorated method to ensure it receives the owner (class) as the first argument."""
            return self.decorated_method(owner, *args, **kwargs)
        
        return wrapper
