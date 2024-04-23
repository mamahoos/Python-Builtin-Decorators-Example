from Wraps import Wraps


def Final(func: callable):
    # Mark the function as final, preventing it from being overridden
    func.__final__ = True
    # Define a wrapper function that will wrap the original function
    def wrapper(*args, **kwargs):
        # Call the original function with any arguments and keyword arguments
        return func(*args, **kwargs)
    # Return the wrapper function, now decorated with 'Wraps' to preserve metadata
    return Wraps(func)(wrapper)