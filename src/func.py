import math
import eval
from node import Unit

def addtion(args: list[Unit]):
    resArr = []
    for arg in args:
        resUnit = eval.evaluate(arg)
        resArr.append(resUnit.value)
    result = Unit(sum(resArr))
    return result

def subtraction(args: list[Unit]):
    if(len(args) != 2):
        raise TypeError("List contains more than 2 values!")
    leftVal = eval.evaluate(args[0]).value 
    rightVal = eval.evaluate(args[1]).value
    result = Unit(leftVal - rightVal)
    return result

def multiplacation(args: list[Unit]):
    result = 1
    resArr = []
    for arg in args:
        resUnit = eval.evaluate(arg)
        resArr.append(resUnit.value)
    result = Unit(math.prod(resArr))
    return result

def divition(args: list[Unit]):
    if(len(args) != 2):
        raise TypeError("List contains more than 2 values!")
    leftVal = eval.evaluate(args[0]).value 
    rightVal = eval.evaluate(args[1]).value
    result = Unit(int(leftVal / rightVal))
    return result
