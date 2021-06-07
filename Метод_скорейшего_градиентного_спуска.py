import numpy as np

def f(n, a, b, e, xt):
    x = np.array(np.zeros(n))
    x=[0.3, -0.05, -0.2, 0.3]
    t=False
    k=0
    while(t==False):
        r=(a.dot(x)-b)
        print('r, ', r)
        u=(r*(a.dot(r.dot(a.transpose()))))/((a.dot(r.dot(a.transpose())))*(a.dot(r.dot(a.transpose()))))
        x=x-u*a.transpose().dot(r)
        k+=1
        print(x)
        t=True
        for i in range(n):
            if (abs(xt[i]-x[i])>e):
                t=False
    print(k, " итераций, для достижения точности e =", e)    
    return x


print("z")

e=0.001

a= [[8, -1, -2, 0],
    [0, 10, -2, 2],
    [-1, 0, 6, 2],
[3, -1, 2, 12]]




b=[-2.3, 0.5, 1.2, -3.7]


n=len(b)

xt=np.linalg.solve(a, b)
f(n, np.array(a), np.array(b), e, xt)

print(np.linalg.solve(a, b))
