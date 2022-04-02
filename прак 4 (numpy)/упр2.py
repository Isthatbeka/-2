import numpy as np

def reading(name):
    data = open(name, "r").readlines()
    x=[]
    for i1 in range(len(data)):
        buf = data[i1].split()
        for j in range(len(buf)):
            x.append(float(buf[j]))
    x=np.array(x)
    return x, len(buf)
x11,a11=reading('ex2_1.txt')
x1=x11.reshape(int(len(x11)/a11), a11)
print(x1)
x22,a22=reading('ex2_2.txt')
x2=x22.reshape(int(len(x22)/a22), a22)
meanx1=x1.mean(axis=0)
meanx2=x2.mean(axis=0)
print('Cреднее по ex2_1: ', meanx1)
print('Cреднее по ex2_2: ', meanx2)
