from statistics import calcAverage
from statistics import relativeCoeff

# print( calcAverage([1,2,3,4,5]))


def testRelativeCoeff():
    ary1 = [1,2,3,4]
    ary2 = [100, 305, 560, 790]

    relCoef = relativeCoeff(ary1, ary2)
    print('relative coef :' + str(relCoef))

testRelativeCoeff()