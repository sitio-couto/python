# from collections import Counter

def getEven(l):
    return [x for x in l if x%2 == 0]

def getEvenPos(l):
    return l[0::2]

def countDict(l):
    dic = {key : 0 for key in l}
    for i in l: dic[i] += 1
    return dic

# def countDict2(l):
#     return Counter(l)

def getMaxVal(d):
    return max(d)

def getMode(l):
    return getMaxVal(countDict(l))

def subList(l, s):
    return any ( l[i:len(s)+i]==s for i in range(len(l)) )

def intersect(a, b):
    return any ( a[i:]==b[:len(a)-i] for i in range(len(a)-len(b),len(a)))

### DECORATORS #################################################################

def time_decorator(function):
    import time

    def wrapper(*args):
        ti = time.time()
        ret = function(*args)
        print("Execution time for ",function.__name__,":", time.time() - ti)
        return ret

    return wrapper

class log_decorator(object):

    def __init__(self, f):
        self.calls = []
        self.f = f

    def __call__(self, *args):
        from datetime import datetime
        now = datetime.now()
        ret = self.f(*args)
        self.calls.append(["Date: "+now.strftime("%Y-%m-%d %H:%M"),
                           "Arguments: "+str(args),
                           "Return: "+str(ret)])
        return ret

    def find_call(self, i):
        print(self.calls[i-1][0])
        print(self.calls[i-1][1])
        print(self.calls[i-1][2])


def dicionary_decorator(function):
    dic = {}

    def wrapper(*args):
        if (dic.get(args, False)):
            ret = dic.get(args)
        else:
            ret = function(*args)
            dic.update({args:ret})

        return ret

    return wrapper

def log_file(file_name):
    def logfile_decorator(function):
        from datetime import datetime
        file = open(file_name, 'a')

        def wrapper(*args, **kwargs):
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            msg = "Call time: " + now + "\nArguments: " + str(args) + "\n\n"
            file.write(msg)
            return function(*args)

        return wrapper
    return logfile_decorator


@log_file("function_log.txt")
def sub(a, b):
    return a - b

@dicionary_decorator
def adding(a, b):
    from time import sleep
    sleep(2)
    return a + b

@log_decorator
def dummy(val):
    print(val)

@log_decorator
def dummyb(val, dd, ddd):
    print(val, dd, ddd)
    return "naice"
