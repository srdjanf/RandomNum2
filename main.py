from random import *
"""
The class does not need any attributes. Just so it works better I have added attributes to the method itself.
We make any variable Rnumber class and invoke random number with 3 attributes.
Minimum number that can be printed, maximum number that can be printed and the amount of numbers printed.
The numbers printed do not need to be different
"""
class Rnumber:
    def __init__(self, something = 1):
        self.something = something
"""
With the random() method we get a number between 0 and 1. We multiply it with 100 to get a precentage.
Then we devide it with 100 - difference between max and min number. 
This gives us the chance to get each number that is between min and max.
After we get the number between 0 and max-min we add the result to the min and round it up. 
"""
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




