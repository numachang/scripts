from sympy import summation,Symbol

def sigma(a,f):
    return a + summation(f ,(n,1,n-1))

n = Symbol("n")
exp = 4*n +1
print(sigma(0,sigma(1,exp)))