import matplotlib.pyplot as plt
import matplotlib
import time
import math
import random
def base3_layer():
    fig = plt.figure(figsize=(10,8),dpi=100,facecolor='red')
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax1.spines['bottom'].set_visible(False)
    ax1.set_xticks(range(4))
    ax1.set_xticklabels(list('abcd')) #文字性描述
    # ax1.grid(axis ='x')
    ax1.grid()#网格线
    ax1.plot([x for x in range(4)],[x for x in range(4)],label = 'tempery')#绘制划线
    ax1.legend(loc = 'lower center')#绘制图例
    ax1.set_title('asdfadsf')#设置表头
    fig.show()

def plot_syn():
    fig = plt.figure(figsize=(10,6),dpi=80)
    x = range(2,26,2)
    y =[random.randint(0,30) for _ in range(12)]
    set_xticklabels = ['h{}'.format(i) for i  in x ]
    plt.xticks(x,set_xticklabels)
    plt.xlabel('time')
    plt.ylabel('时间')
    plt.plot(x,y)
    plt.show()

def plotsin():
    fig = plt.figure(figsize=(10,6),dpi=80)
    x = [i /1000 for i in (range(0,int(4000 * math.pi)))]
    y = [math.sin(_) for _ in x]
    xticks = [i*math.pi/2 for i in range(9)]
    xticklabels = [r'${%d}\pi$' %(i//2) if  i %2 ==0 else r'$\frac{%d}{2}\pi$'%i for i in range(9)]
    plt.xticks(xticks, xticklabels)
    plt.ylabel('sin(x)')
    plt.xlabel('弧度值')
    plt.title('两个正弦曲线')
    plt.plot(x, y,color= 'blue',linestyle = ':',alpha = 0.4)
    plt.show()

def npy():
    fig = plt.figure(figsize=(10,6),dpi=80)
    x = [i  for i in (range(10,30))]
    y = [random.randint(0,2) for i in range(20)]

    xticklabels = ['%d岁' %i for i in x]
    plt.xticks(x, xticklabels,rotation = 45)
    plt.yticks(y)
    plt.ylabel('个数')
    plt.xlabel('年龄')
    plt.title('感情走势')
    plt.plot(x, y,color= 'blue',linestyle = ':',alpha = 0.8)
    plt.show()
    plt.savefig('D://Dell')

if __name__ == '__main__':
    npy()
# time.sleep(5)
#
# fig2 = plt.figure(figsize=(10,8),dpi=40)
# ax1 = fig2.add_subplot(121)
# ax2 = fig2.add_subplot(122)
# fig2.show()