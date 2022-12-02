
from cProfile import run
from multiprocessing import Value
from operator import index
import re
import scikitLern as sc
import busniessKpi as bKpi


großesMoin =[20,30,55,100]

a = [5,5]

#print(sc.machenSachen(großesMoin))


#ac1100 = sc.Schiff.Sägelfläche(22 , 33)
#print(ac1100)


#print(sc.Statistik.satzVonbayesGzahlig(10,8,7,6))

#a = bKpi.basics.endwert_ZW(100, 2, 2)

#print(a)

#jup = bKpi.shares.investmentProYear(a,2,3)

#

#print(jup)

div = [5,5]
#re = 2
#p = 3


#n = 1
#for n in range(0,len(div)):
#    f = lambda x : x/((1+re)**n)
#    newlist = list(map(f,div))
#    n = n + 1
#    #print(n)
#newValue = sum(newlist) + (p / ((1+re)**n))

#print(n)
#print(newValue)



data02 = [5,5,5,6,6,6,6]

ex = bKpi.expo(div, 0.05, 100)
ey = bKpi.expo(data02, 0.05, 100)
print(ex)
print(ey)

#sun = []
#for i in range(0,len(div)):
#    k = div[i] / ex[i]
#    sun.append(k)
#sumNew = sum(sun) + 1




p = lambda x : x/2
g = list(map(p,div))


a = bKpi.basics.rateOfReturn(5,5)

#print(n)
print(a)