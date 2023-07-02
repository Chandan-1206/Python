# access modifiers
# all are public by default
# '_'(underscore) in preffix is used for protected but just as a name convention(indication) it does not restrict anything
# '__'(double underscore) in preffix is used for private but it is not a strict concept in python and can still be
# accessed by name mangling(using '_classname' in preffix when calling )
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # protected name convention
# print(my_object.__mangled_attribute) # Throws an AttributeError (private)
print(my_object._MyClass__mangled_attribute) # mangling
