from typing import Callable
from Wraps import Wraps


def Partial(func: Callable, *args, **kwargs):
    # Store the arguments and keyword arguments provided to the decorator.
    p_args, p_kwargs = args, kwargs
    
    # Define the wrapper function that will be called with the remaining arguments.
    def wrapper(*args, **kwargs):
        # Call the original function with the stored arguments combined with the new ones.
        return func(*p_args, *args, **p_kwargs, **kwargs)
    
    # Use the wraps decorator from functools to preserve the metadata of the original function.
    return Wraps(func)(wrapper)
