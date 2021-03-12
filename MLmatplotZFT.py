import matplotlib.pyplot as plt
import  numpy as np
def ex1():
    march = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
    october = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

    fig = plt.figure(figsize=(10,8),dpi=80)

    ax1 = fig.add_subplot(221)
    ax1.scatter(range(len(march)),march)



    ax2 = fig.add_subplot(222)
    march_x = range(len(march))
    # ax2.scatter((),march)
    ax2.scatter(range(40,40+len(october)),october)


    ax3 = fig.add_subplot(223)
    march_x = range(len(march))
    october_x = [i+40 for i  in march_x]
    ax3.scatter(march_x,march)
    ax3.scatter(october_x,october)


    ax4 = fig.add_subplot(224)
    march_labels = ['3月%d日'%(i+1) for i in march_x]
    october_labels = ['10月%d日'%(i+1-40) for i in october_x]
    ax4.set_xticks(list(march_x)[::5] + october_x[::5])
    ax4.set_xticklabels(march_labels[::5] +october_labels[::5],rotation = 45 )

    ax4.scatter(march_x,march)
    ax4.scatter(october_x,october)

    # plt.show()

    a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊"]

    b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

    fig  = plt.figure(figsize=(10,8),dpi =80)
    ax1 =fig.add_subplot()
    ax1.bar(a,b,width=0.2,color = 'orange')
    ax1.set_xticks(range(len(a)))
    ax1.set_xticklabels(a,rotation = 80)
    plt.subplots_adjust(bottom = 0.3)
    # plt.show()

def ex2():
    a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
    b_16 = [15746,312,4497,319]
    b_15 = [12357,156,2045,168]
    b_14 = [2358,399,2358,362]
    fig = plt.figure(figsize=(80,10),dpi=80)
    x = range(len(a))
    fig = plt.figure(figsize=(10,8),dpi =80)
    ax1 =fig.add_subplot()
    ax1.bar(x,b_14,width =0.2,label ='9月14日')
    ax1.bar([i + 0.2 for i in x ],b_15,width =0.2,label ='9月14日')
    ax1.bar([i + 0.4 for i in x ],b_16,width =0.2,label ='9月14日')
    # ax1.set_xticks([i+0.2 for i in x])
    ax1.set_xticks(range(len(a)))
    ax1.set_xticklabels(a)
    ax1.legend()
    plt.show()

def ex3():
    a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
    b_16 = [15746, 312, 4497, 319]
    b_15 = [12357, 156, 2045, 168]
    b_14 = [2358, 399, 2358, 362]
    timel = [b_14,b_15,b_16]
    timel = np.array(timel)
    print(timel)
    c = timel.transpose()
    print(c)
    fig = plt.figure(figsize=(10, 8), dpi=80)
    ax1 = fig.add_subplot()
    x= range(len(timel))
    ax1.bar(x, c[0], width=0.2,label ='猩球崛起3：终极之战')
    ax1.bar([i + 0.2 for i in x], c[1], width=0.2,label ='敦刻尔克')
    ax1.bar([i + 0.4 for i in x], c[2], width=0.2,label ='蜘蛛侠：英雄归来')
    ax1.bar([i + 0.6 for i in x], c[3], width=0.2,label ='战狼2')
    time_name= ['9.14','9.15','9.16','4']
    ax1.set_xticks(range(len(c)))
    ax1.set_xticklabels(time_name)
    ax1.legend()
    plt.show()

def zft():
    a = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130,
         124, 101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150, 110,
         117, 86, 95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123, 117, 119,
         105, 137, 123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120,
         114, 105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139, 139, 119,
         140, 83, 110, 102, 123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114, 122, 109,
         106, 123, 116, 131, 127, 115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111, 100, 154,
         136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110, 118, 127,
         121, 114, 125, 126, 114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146, 97, 137,
         105, 98, 117, 112, 81, 97, 139, 113, 134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110, 105, 129,
         137, 112, 120, 113, 133, 112, 83, 94, 146, 133, 101, 131, 116, 111, 84, 137, 115, 122, 106, 144, 109, 123, 116,
         111, 111, 133, 150]
    bin_width =3
    num_bit = int ((max(a)- min(a))/ bin_width)
    plt.hist(a,num_bit)
    plt.xticks(list(range(min(a),max(a)))[::bin_width],rotation = 45)
    plt.show()
    return

zft()