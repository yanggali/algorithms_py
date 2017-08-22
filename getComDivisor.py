'''
求两数的最大公约数
结合1、辗转相除法（位移）和2、更相减法进行优化
时间复杂度：O(log(max(a,b)))
'''
def getMax(numberA,numberB):
    if(numberA == numberB):
        return numberA
    elif(numberA < numberB):
        return getMax(numberB,numberA)
    else:
        if(numberA%2 == 0 and numberB%2==0):
            return 2*getMax(numberA/2,numberB/2)
        elif(numberA%2 == 0 and numberB%2 != 0 ):
            return getMax(numberA/2,numberB)
        elif(numberA%2 != 0 and numberB%2 == 0):
            return getMax(numberA,numberB/2)
        else:
            return getMax(numberA-numberB,numberB)


print(getMax(1000,101))