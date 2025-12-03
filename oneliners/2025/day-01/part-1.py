# unfortunately, no tail recursion in python
import sys
sys.setrecursionlimit(10000)

print((lambda f:lambda n:f(f,n))(lambda f,n,d=50,a=0:f(f,n[1:],r:=(d+n[0])%100,a+(r<1))if n else a)([int(x.strip().replace("L","-").strip("R"))for x in open(0)]))