import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,10)
#
# b = np.ones((3,3)).astype(bool)
# print(b.strides)
# c = np.array([True,True,True])
# # b.dtype =  bool
# print(b)

GBdata = np.loadtxt('GB_video_data_numbers.csv', delimiter=',', dtype= int)
GBcomments = GBdata[:, -1]
GBcomments = GBcomments[GBcomments<10000]

Eglanddata = np.loadtxt('US_video_data_numbers.csv',delimiter=',',dtype= int)
Egcomments = Eglanddata[:, -1]
Egcomments = Egcomments[Egcomments<5000]
likes = Eglanddata[:,1]
Egllikes = Eglanddata[:,2]


fig = plt.figure(figsize=(16,10),dpi=80)
ax1 = fig.add_subplot(221)
bin_width = 500

num_bit = int((max(GBcomments) - min(GBcomments)) / bin_width)
ax1.hist(GBcomments, num_bit)

ax2 = fig.add_subplot(222)
num_bit = int((max(Egcomments) - min(Egcomments)) / bin_width)
ax2.hist(Egcomments, num_bit)

ax3 = fig.add_subplot(223)
ax3.scatter(likes,Egllikes)
plt.show()

# t = np.arange(24).reshape(4,6).astype(float)
# t[1][0] = np.nan
# for i in range(t.shape[1]):
#     nan_num = np.count_nonzero(t[:,i] != t[:,i])#nan的个数
print(np.iszero(a))

np.linspace(5,10)
np.nonzero()
np.argmax