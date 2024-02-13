
def ntimes(f):
    def wrapper(*args,**kwargs):
        for _ in range(2):
            rv = f(*args,**kwargs)
        return rv
    return wrapper

@ntimes
def add(x,y):
    rv = x + y
    print(rv)
    return x + y
@ntimes
def sub(x,y):
    rv = x - y
    print(rv)
    return x - y

add(2,3)
sub(2,3)