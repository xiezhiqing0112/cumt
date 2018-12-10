import math
import numpy as np
import pylab as pl

data=[[1,81] ,[   2 ,   60],
 [    3 ,   64],
 [    4,    90],
 [    5 ,  954],
 [    6,  2026],
 [    7 ,    0],
 [    8,    23],
 [    9 , 3553],
 [   10 ,  277],
 [   11,    13],
 [   12,    48],
 [   13 ,   28],
 [   14  ,  30],
 [   15 ,  44],
 [   16   ,404],
 [   17  , 877],
 [   18   , 37],
 [   19    ,50],
 [   20   , 68],
 [   21   , 24],
 [   22    , 0],
 [   23  , 300],
 [   24   , 14],
 [   25    ,21],
 [   26  ,4195],
 [   27   ,  0],
 [   28    ,79],
 [   29  ,  18],
 [   30  , 984],
 [   31 , 2318],
 [   32  ,   0],
 [   33  ,1648],
 [   34   , 95],
 [   35  , 290],
 [   36   , 39],
 [   37   , 17],
 [   38   , 41],
 [   39 , 5074],
 [   40  ,  89],
 [   41   ,  2],
 [   42    , 0],
 [   43   ,  0],
 [   44 , 6172],
 [   45  ,  57],
 [   46   , 26],
 [   47   , 26],
 [   48   , 46],
 [   49   , 22],
 [   50  ,4219],
 [   51   , 21],
 [   52    ,34],
 [   53 , 1425],
 [   54 , 1578],
 [   55  , 396],
 [   56   ,376],
 [   57   ,  0],
 [   58  ,  38],
 [   59  ,  65],
 [   60  , 378],
 [   61  ,  75],
 [   62  ,  66],
 [   63  , 220],
 [   64  ,  31],
 [   65  ,1331],
 [   66   , 32],
 [   67    , 0],
 [   68   ,234],
 [   69   ,721],
 [   70   ,  0],
 [   71   , 36],
 [   72  ,2752],
 [   73   , 39],
 [   74  , 145],
 [   75  , 114],
 [   76  ,1023],
 [   77  , 155],
 [   78  ,2232],
 [   79  ,   6],
 [   80  ,1854],
 [   81  ,4012],
 [   82 ,11464],
 [   83  ,   0],
 [   84   , 17],
 [   85   , 84],
 [   86   ,143],
 [   87  ,1733],
 [   88 ,   77],
 [   89  , 106],
 [   90  , 640],
 [   91  ,   8],
 [   92  , 415],
 [   93  ,  77],
 [   94  ,   0],
 [   95  ,1704],
 [   96  ,  53],
 [   97  , 133],
 [   98  ,   0],
 [   99  ,  54],
 [  100  ,2577],
 [  101  ,1988],
 [  102  ,   0],
 [  103  ,5219],
 [  104  ,   0]]
print(len(data))
dataset = [(float(data[i][0]), float(data[i][1])) for i in range(0, len(data))]
print(type(dataset))
 #计算欧几里得距离,a,b分别为两个元组
def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2)+math.pow(a[1]-b[1], 2))

#算法模型
def DBSCAN(D, e, Minpts):
    #初始化核心对象集合T,聚类个数k,聚类集合C, 未访问集合P,
    T = set(); k = 0; C = []; P = set(D)
    for d in D:
        if len([ i for i in D if dist(d, i) <= e]) >= Minpts:
            T.add(d)
    #开始聚类
    while len(T):
        P_old = P
        o = list(T)[np.random.randint(0, len(T))]
        P = P - set(o)
        Q = []; Q.append(o)
        while len(Q):
            q = Q[0]
            Nq = [i for i in D if dist(q, i) <= e]
            if len(Nq) >= Minpts:
                S = P & set(Nq)
                Q += (list(S))
                P = P - S
            Q.remove(q)
        k += 1
        Ck = list(P_old - P)
        T = T - set(Ck)
        C.append(Ck)
    return C

#画图
def draw(C):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(C)):
        coo_X = []    #x坐标列表
        coo_Y = []    #y坐标列表
        for j in range(len(C[i])):
            coo_X.append(C[i][j][0])
            coo_Y.append(C[i][j][1])
        pl.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)

    pl.legend(loc='upper right')
    pl.show()




C = DBSCAN(dataset, 200, 2)
print(C)
draw(C)
