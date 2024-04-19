from typing import Callable, Any, Self


class Property:
    def __init__(
        self,
        fget: Callable[Any, Any | None] = None,
        fset: Callable[Any, Any | None] = None,
        fdel: Callable[Any, Any | None] = None,
        doc: str = None
    ) -> None:
        """Initialize the Property decorator.
        
        Args:
            fget (Callable[..., Any | None], optional): The getter method for the property.
            fset (Callable[..., Any | None], optional): The setter method for the property.
            fdel (Callable[..., Any | None], optional): The deleter method for the property.
            doc (str, optional): The docstring for the property.
        """
        self.cls = type(self)  # Store the class type of the instance.
        self.fget = fget  # The getter method.
        self.fset = fset  # The setter method.
        self.fdel = fdel  # The deleter method.
        self.__doc__ = doc or fget.__doc__  # The docstring for the property.
        self.__name__ = fget.__name__  # The name of the property.

    def __get__(self, instance, owner):
        """Define behavior for when the property is accessed.
        
        Args:
            instance: The instance that the property is accessed through.
            owner: The owner class of the instance.
            
        Returns:
            The value returned by the getter method.
            
        Raises:
            AttributeError: If the property is not readable.
        """
        if instance is None:
            return self  # Return the property itself if accessed through the class.
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)  # Call the getter method.

    def __set__(self, instance, value):
        """Define behavior for when the property is set.
        
        Args:
            instance: The instance on which the property is set.
            value: The new value for the property.
            
        Raises:
            AttributeError: If the property cannot be set.
        """
        if self.fset is None:
            raise AttributeError("can't set attribute")
        return self.fset(instance, value)  # Call the setter method.

    def __delete__(self, instance):
        """Define behavior for when the property is deleted.
        
        Args:
            instance: The instance on which the property is deleted.
            
        Raises:
            AttributeError: If the property cannot be deleted.
        """
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)  # Call the deleter method.

    def getter(self, accessor: Callable[Any, Any | None]) -> Self:
        """Define a new getter for the property.
        
        Args:
            accessor (Callable[Any, Any | None]): The new getter method.
            
        Returns:
            A new Property instance with the updated getter.
        """
        self.__doc__ = accessor.__doc__ or self.__doc__  # Update the docstring.
        self.__name__ = accessor.__name__  # Update the name.
        return self.cls(accessor, self.fset, self.fdel, self.__doc__)  # Return a new Property with the new getter.

    def setter(self, accessor: Callable[Any, Any | None]) -> Self:
        """Define a new setter for the property.
        
        Args:
            accessor (Callable[Any, Any | None]): The new setter method.
            
        Returns:
            A new Property instance with the updated setter.
        """
        return self.cls(self.fget, accessor, self.fdel, self.__doc__)  # Return a new Property with the new setter.

    def deleter(self, accessor: Callable[Any, Any | None]) -> Self:
        """Define a new deleter for the property.
        
        Args:
            accessor (Callable[Any, Any | None]): The new deleter method.
            
        Returns:
            A new Property instance with the updated deleter.
        """
        return self.cls(self.fget, self.fset, accessor, self.__doc__)  # Return a new Property with the new deleter.
