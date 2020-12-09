#!/usr/bin/env python

import math
import sys


def gcdExtended(a, b):  
    print("gcdExtended")
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y

def egcd(a, b):
    r = [a, b]
    x = [1, 0]
    y = [0, 1]
    i = 2
    while (r[i-2] % r[i-1]) > 0:
        print("egcd")
        print(r)
        rt = r[i-2] % r[i-1]
        r.append(rt)
        xt = (x[i-2] - math.floor(r[i-2] // r[i-1]) * x[i-1])
        x.append(xt)
        yt = (y[i-2] - math.floor(r[i-2] // r[i-1]) * y[i-1])
        y.append(yt)
        
        i += 1

    print("%s * %s + %s * %s" % (a, x[-1], b, y[-1]))
    return(x,y)

print(egcd(int(sys.argv[1]), int(sys.argv[2])))
print(gcdExtended(int(sys.argv[1]), int(sys.argv[2])))
