from random import *


class Rnumber:
    def __init__(self,minnum,maxnum, amount):
        self.minnum = minnum
        self.maxnum = maxnum
        self.amount = amount


    def randomNumber(self, minnum = None, maxnum = None, amount = None):
        if minnum == None:
            minnum = self.minnum
            maxnum = self.maxnum
            amount = self.amount
        x = amount
        while x > 0:
            r = random()
            prec_diff = (r * 100) / (100 / (maxnum - minnum))
            res = minnum + prec_diff
            print(round(res))
            x = x - 1


a = Rnumber(4, 16, 2)

a.randomNumber()






