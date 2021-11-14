from random import *

class Rnumber:
    def __init__(self, something = 1):
        self.something = something

    def randomNumber(self, minnum, maxnum, amount):
        x = amount
        while x > 0:
            r = random()
            prec_diff = (r * 100) / (100 / (maxnum - minnum))
            res = minnum + prec_diff
            print(round(res))
            x = x - 1


a = Rnumber()

a.randomNumber(4, 16, 3)




