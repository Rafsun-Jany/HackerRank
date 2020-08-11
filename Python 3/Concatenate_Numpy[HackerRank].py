import numpy as np

n,m,p = map(int,input().split())
k = n+m
arr = np.array((input().split()),int)
for i in range(k-1):
    arr_new = np.array((input().split()),int)
    arr = np.concatenate((arr,arr_new))
print(arr.reshape((k,p)))
