import time

class logstr(object):

    def __init__(self, f):
        self.log = ""
        self.f = f

    def __call__(self, *args):
        ret = self.f(*args)
        self.log += time.asctime(time.localtime())
        self.log += " entrada: " + str(args) + " saida: " + str(ret) + "\n"
        return ret
#
# def logstr(function):
#     log = "\n"
#
#     def wrapper(*args):
#         ret = function(*args)
#         log += time.asctime(time.localtime())
#         # log += " Entrada: " + str(args) + " Return: " + str(ret) + "\n"
#         return ret
#
#     return wrapper

@logstr
def add(a, b):
    return a+b
