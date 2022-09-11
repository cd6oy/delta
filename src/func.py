import math
import eval
from node import Unit

def addtion(args: list[Unit], ctx: dict[str, Unit]):
    resArr = []
    for arg in args:
        resUnit = eval.evaluate(arg, ctx)
        resArr.append(resUnit.value)
    result = Unit(sum(resArr))
    return result

def subtraction(args: list[Unit], ctx: dict[str, Unit]):
    if(len(args) != 2):
        raise TypeError("List should have 2 values!")
    leftVal = eval.evaluate(args[0], ctx).value 
    rightVal = eval.evaluate(args[1], ctx).value
    result = Unit(leftVal - rightVal)
    return result

def multiplacation(args: list[Unit], ctx: dict[str, Unit]):
    result = 1
    resArr = []
    for arg in args:
        resUnit = eval.evaluate(arg, ctx)
        resArr.append(resUnit.value)
    result = Unit(math.prod(resArr))
    return result

def divition(args: list[Unit], ctx: dict[str, Unit]):
    if(len(args) != 2):
        raise TypeError("List should have 2 values!")
    leftVal = eval.evaluate(args[0], ctx).value 
    rightVal = eval.evaluate(args[1], ctx).value
    result = Unit(int(leftVal / rightVal))
    return result

def sequence(args: list[Unit], ctx: dict[str, Unit]):
    l = []
    for arg in args:
        lu = eval.evaluate(arg, ctx)
        l.append(lu)
    result = l[len(l)-1]
    return result

def define(args: list[Unit], ctx: dict[str, Unit]):
    if(len(args) != 2):
        raise TypeError('List should have 2 values!')
    else:
        leftVal = args[0].value
        rightUnit = eval.evaluate(args[1], ctx)
        ctx[leftVal] = rightUnit
        result = rightUnit
        return result

def length(args: list[Unit], ctx: dict[str, Unit]):
    if(len(args) != 1):
        raise TypeError("List should have 1 Value!")
    unitVal = eval.evaluate(args[0], ctx).value
    result = Unit(len(unitVal[1:-1]))
    return result