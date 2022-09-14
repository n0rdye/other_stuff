a=2
b=3
e=0.0001

def f(x):
    return (x-2)**2 * 2**x -1

    
while True:
    c=(a+b)/2
    print(a,"|",b,"|",c,"\n")
    
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
        
    if not b-a>e:
        print(round((a+b)/2,3))
        print(round((b-a)/2,3))
        break
