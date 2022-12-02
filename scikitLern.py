


def summe(a, b):
    c = a + b
    return c


def kreis(r):
    pi = 3.1415
    k = 4/3 * pi * r ** 3
    return k


eimer = [1,2,3,4,5]

def machenSachen(a):
    neuEimer =[]
    for i in a:
        if i < 2:
            neuEimer.append(kreis(i))
        else:
         neuEimer.append(i+10)
    return neuEimer


#print(machenSachen(eimer))


class Schiff():
    def Sägelfläche(h , b):
        return h * b + 2 


class Statistik():

    def satzVonbayesProzent(pa, pb, pab ):
        sVb = (pa * pb) / pab
        return sVb

    def satzVonbayesGzahlig(n , a , b , c):
        svb = ((a/n) * (b/n)) / (c/n)
        return svb

