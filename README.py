##._variable is semiprivate and meant just for convention
##.__variable is often incorrectly considered superprivate, while it's actual meaning is just to namemangle to prevent accidental access[1]
##.__variable__ is typically reserved for builtin methods or variables
##You can still access .__mangled variables if you desperately want to. The double underscores just namemangles, or renames, the variable to something like instance._className__mangled
##Example:
##class Test(object):
##    def __init__(self):
##        self.__a = 'a'
##        self._b = 'b'
##
##>>> t = Test()
##>>> t._b
##'b'
##t._b is accessible because it is only hidden by convention
##>>> t.__a
##Traceback (most recent call last):
##  File "<stdin>", line 1, in <module>
##AttributeError: 'Test' object has no attribute '__a'
##t.__a isn't found because it no longer exists due to namemangling
##>>> t._Test__a
##'a'
##By accessing instance._className__variable instead of just the double underscore name, you can access the hidden value

