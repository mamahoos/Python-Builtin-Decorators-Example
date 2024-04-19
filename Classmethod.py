from functools import wraps
from typing import Callable


class Classmethod:

    def __init__(self, decorated_method: Callable):
        self.decorated_method = decorated_method
        
    def __get__(self, instance, owner):
        
        @wraps(self.decorated_method)
        def wrapper(*args, **kwargs):
            return self.decorated_method(owner, *args, **kwargs)
        
        return wrapper
