import numpy as np

#1
a = np.zeros(10)
a[5] =1
print(a)

#2
ten = np.arange(10,50,1)
print(ten)

#3
ten = np.flip(ten,axis = 0)
print(ten)

#4
tenL = np.random.randint(0,100,(10,10),int)
print(np.max(tenL))
print(np.min(tenL))

#5
tenP = np.ones((10,10))
tenP[1:-1:,1:-1] =0
print(tenP)

tenP = np.zeros((10,10))
tenP[[0,-1],:] =1
tenP[:,[0,-1]] =1
print(tenP)

#6
five = np.array([[ i  for i in range(5)] for _  in range(5)])
print(five)

#7
dengcha = np.linspace(0,1,12)
print(dengcha)

#8
suiji = np.random.random(10)

print(sorted(suiji))

#9
sui_ji = np.random.random(10)
k = np.max(sui_ji)
sui_ji[sui_ji == sui_ji.max()] = 99


#10
a = np.random.random(10)
a[np.argsort(a[:,2])]#利用切片对数据进行排序

#11
