"""
    1. Everything in python is object. Such as integer, strings, functions, classes etc
    2. type() can be used as a function as well as a class creator
    3. When used as a function it tells the type/class of the object
    4. To use type() as function we pass the object as parameter - type(5), type("myclass"), type(fun)
    5. To use as a class creator :
        myclass = type("myclass", (), {})
        type(classname: str, base_classes: Tuple[classnames], attributes: Dict())
    6. Whenever we create a class, its meta class is called which returns the object i.e the class.
    7. __new__() is used to assign memory to object and modfy various attributed of the class
    8. __init__() is used to initialize the object attributes
    9. User-defined metaclass - 
        def Meta(type):
        def __new__(cls):
            pass
    10. Using user-defined metaclass in your class - 
        class MyClass(metaclass = Meta):
            pass
"""