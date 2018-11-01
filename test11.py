import time
import functools

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
