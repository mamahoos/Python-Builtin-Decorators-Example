from typing import Literal, Callable


WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', 
                       '__doc__', '__annotations__')
WRAPPER_UPDATES = ('__dict__',)

def Wraps(wrapped: Callable,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):
    
    def wrraper(decorator: Callable):
        for attr in assigned:
            attr_value = getattr(wrapped, attr)
            setattr(decorator, attr, attr_value)

        for attr in updated:
            attr_value = getattr(wrapped, attr, {})
            updeted_attr = getattr(decorator, attr)
            updeted_attr.update(attr_value)

        return decorator
    return wrraper