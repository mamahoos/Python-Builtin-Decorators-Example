from typing import Callable


class Staticmethod:
  
    def __init__(self, decorated_method: Callable):
        self.decorated_method = decorated_method
        
    def __get__(self, instance, owner):
        return self.decorated_method
    

