class A:
    x = 1

class B(A):
    pass

class C(A):
    pass

print(A.x, B.x, C.x)

B.x = 2
print(A.x, B.x, C.x)

A.x = 3
print(A.x, B.x, C.x) # C.x changed, but B.x didn't

a = A()
print(a.x, A.x)

a.x += 1
print(a.x, A.x)