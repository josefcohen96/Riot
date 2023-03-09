# import os
# import sys
import re
from typing import Optional, Any


#
# current_path = os.path.realpath(os.path.dirname(_file_))
#
# if sys.platform == "linux" or sys.platform == "linux2":
#     sys.path.append(current_path)  # to self
# else:
#     sys.path.append(r"%s\..\.." % current_path)  # to ng_automation

# from global_package.generic.Global import Global
# from global_package.generic.LogFunctions import log_debug, log_info


# class Result(Global):
class Result:
    """Generic class to return result from function or method"""

    # class ErrorCode(Global):
    class ErrorCode:
        """ENUM error codes"""
        ok = 0
        error = 1
        timeout = 2
        exception = 3
        not_ran = 4
        unimplemented = 5
        unsupported = 6
        unknown = 7

        # def _init_(self):
        #     Global._init_(self)

    def __init__(self, error: Optional[ErrorCode] = None, error_msg: str = "", value: Optional[Any] = None, *args,
                 **kwargs):
        # Global._init_(self)
        self.error = error
        self.error_msg = error_msg
        self.value = value

    def __add__(self, other, *args, **kwargs):
        if self.error > other.error:
            error = self.error
        else:
            error = other.error

        error_msg = self.error_msg + "\n" + other.error_msg
        value = other.value
        return Result(error=error, error_msg=error_msg, value=value)

    def __str__(self, *args, **kwargs):
        value = "<%s:" % self.__class__.__name__
        var_list = vars(self)
        for var in var_list:
            if not re.match("__", var):  # not strong privates
                val = eval("self.%s" % var)

                if hasattr(self, "father"):
                    if val == self.father:
                        continue  # circular recursion on str(var) calling my father

                value += " %s=%s," % (str(var), str(val))

        value = value[:-1]
        value += ">"
        return value


# ########################################################
# EXAMPLE CODE
# ########################################################
if __name__ == '__main__':
    pass
    # result = Result(error=Result.ErrorCode.ok, error_msg="all good", value="7")
    # result += Result(error=Result.ErrorCode.error, error_msg="some error", value=None)
    # result += Result(error=Result.ErrorCode.unknown, error_msg="???", value=12.1)
    #
    # print(result)

