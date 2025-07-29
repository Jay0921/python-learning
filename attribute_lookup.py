    #         Attribute Lookup (obj.x)
    #              |
    #              v
    # Is x a data descriptor in class?
    #       |         |
    #      Yes       No
    #       |         v
    # Call __get__   Is x in obj.__dict__?
    #                  |        |
    #                 Yes      No
    #                  |        |
    #             Return it   Is x a non-data descriptor?
    #                              |         |
    #                             Yes       No
    #                              |         |
    #                       Call __get__   Look in base classes...

# | You define...            | What you get             | Descriptor Type     |
# | ------------------------ | ------------------------ | ------------------- |
# | `@property` only         | `__get__` only           | Non-data descriptor |
# | `@property` + `@setter`  | `__get__` + `__set__`    | ✅ Data descriptor   |
# | `@property` + `@deleter` | `__get__` + `__delete__` | ✅ Data descriptor   |
# | Regular method           | `__get__` only           | Non-data descriptor |


class Person:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def greet(self):
        return "Hello"

person = Person()


# Both regular methods and properties are stored in the class’s __dict__
print(type(Person.__dict__['name']))
# <class 'property'>
print(type(Person.__dict__['greet']))
# <class 'function'>

# Overriding a function with a string and then trying to call it will raise a TypeError.
# person.greet = 'sleep'
# print(person.greet())
# TypeError: 'str' object is not callable

# Now the greet method is holding a string instead of a method,
# and we can simply access it as an attribute.
# print(person.greet)
# sleep

breakpoint()
