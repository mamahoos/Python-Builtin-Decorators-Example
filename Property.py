from typing import Callable, Any


class Property:

    def __init__(
        self,
        fget: Callable[..., Any | None] = None,
        fset: Callable[..., Any | None] = None,
        fdel: Callable[..., Any | None] = None,
        doc: str = None
    ) -> None:
        self.cls = type(self)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__

    def __get__(self, instance, _: "instance_type"):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def getter(self, accessor: Callable[Any, Any | None]) -> "Property":
        self.__doc__ = accessor.__doc__ or self.__doc__
        self.__name__ = accessor.__name__
        return self.cls(accessor, self.fset, self.fdel, self.__doc__)

    def setter(self, accessor: Callable[Any, Any | None]) -> "Property":
        return self.cls(self.fget, accessor, self.fdel, self.__doc__)

    def deleter(self, accessor: Callable[Any, Any | None]) -> "Property":
        return self.cls(self.fget, self.fset, accessor, self.__doc__)
