from time import sleep
def compute():
    for i in range(10):
        sleep(.5)
        yield i

for x in compute():
    print(x)
print('finished')