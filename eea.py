#!/usr/bin/env python

import math
import sys


def egcd(a, b):
    r = [a, b]
    x = [1, 0]
    y = [0, 1]
    i = 2
    while (r[i-2] % r[i-1]) > 0:
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
