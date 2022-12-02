



from hashlib import new


class basics():
    
    def EBITDA(profit, interest, tax, depreciation, amortisation):
        EBITDA = profit + interest + tax + depreciation + amortisation
        return EBITDA

    def EBIT(profit, interest, tax):
        EBIT = profit + interest + tax 
        return EBIT

    def rateOfReturn(netProfit, sales):
        return netProfit / sales

    def corporateValue(eK, fK, cash):
        return (eK+fK)-cash

    def annuität_BW(c,r,n):
        return c * (1/r) * (1-(1/(1+r**n)))

    def endwert_ZW(c,r,n):
        return c * (1/r) * (1 + ((r**n) - 1))

    def geometWachsendeEwigeRente(c,r,g):
        return c / (r - g)

    def geometWachsendeEwigeAnnuite(c,r,g,n):
        return c / (1/(r - g)) * (1-((1+g)/(1+r)**n))


class zinsen():

    def nominalToEffekive(rnom, k):
        return (1 + (rnom/k))**k
    
    def effekiveToNominal(reff, k):
        return ((1 + (reff/k))**k) -1


class kedite():
    
    def BW(c, r, n):
        return c * (1/r**n) * (1 - (1/(1+r)**n))


class anleihe():
    def kuponzahlung(kZins, Nennwert, anzahlZahlungen):
        return (kZins * Nennwert) / anzahlZahlungen
    
    def nullkuponanPreis(NOM, reff):
        return NOM / (1+reff)

    def kuponanPreis(k, y, n, NOM):
        p = k * (1/y) * (1 - ((1/(1+y))**n)) + (NOM / (1 + y)**n)
        return p


class shares():

    def investmentProYear(div, p, re):
        n = 1
        for n in range(0,len(div)):
            f = lambda x : x/((1+re)**n)
            newlist = list(map(f,div))
            n = n + 1
        newValue = sum(newlist) + (p / (1+re))**n
        return newValue, n



def expo(value, re, preis):
    a=[]
    c=[]
    for i in range(0,len(value)):
        a.append(i+1)
    
    for e in range(0,len(value)):
        f = (1 + re) ** a[e]
        c.append(f)
    
    sun = []
    for i in range(0,len(value)):
        k = value[i] / c[i]
        sun.append(k)
    sumNew = round(sum(sun) + preis / ((1+re)**len(value)))

    return sumNew




class Statistik():

    def mittel(a):
        listsum = 0
        for i in a:
            listsum += i
        return listsum/len(a)
            
    def A_mittel(a):
        return sum(a)/len(a)



    