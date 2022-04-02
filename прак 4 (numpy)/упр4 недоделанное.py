import numpy as np

def reading(name):
    data = open(name, "r").readlines()
    x=[]
    for i1 in range(len(data)):
        buf = data[i1].split()
        x.append(float(buf[0]))
    return x
file=reading('ex4.txt')
print('среднее:', str(np.mean(file)))
print('стандартное отклонение:', np.std(file))

file.sort()
