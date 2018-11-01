import time
import functools

# class logstr(object):
#
#     def __init__(self, f):
#         self.log = ""
#         self.f = f
#
#     def __call__(self, *args):
#         ret = self.f(*args)
#         self.log += time.asctime(time.localtime())
#         self.log += " entrada: " + str(args) + " saida: " + str(ret) + "\n"
#         return ret

def logstr(function):
    @functools.wraps(function)
    def wrapper(*args):
        ret = function(*args)
        wrapper.log += time.asctime(time.localtime())
        wrapper.log += " entrada: " + str(args) + " saida: " + str(ret) + "\n"
        return ret
    wrapper.log = ""
    return wrapper

@logstr
def add(a, b):
    return a+b
