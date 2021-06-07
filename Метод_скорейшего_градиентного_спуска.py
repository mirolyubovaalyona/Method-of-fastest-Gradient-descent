import numpy as np

def f(n, a, b, e, xt):
    x = np.array(np.zeros(n))
    t=False
    k=0
    while(t==False):
        r=(a.dot(x)-b)
        u=(r*r)/(a.dot(r)*r)
        #grad f(x)=2(Ax-b)
        x=x-u*r
        k+=1
        print(x)
        t=True
        for i in range(n):
            if (abs(xt[i]-x[i])>e):
                t=False
    print(k, " итераций, для достижения точности e =", e)    
    return x




e=0.001

a=[[20, 2, 3, 7],
[1, 12, -2, -5],
[5, -3, 13, 0],
[0, 0, -3, 15]]




b=[5, 4, -3, 7]



n=len(b)

xt=np.linalg.solve(a, b)
f(n, np.array(a), np.array(b), e, xt)

print(np.linalg.solve(a, b))