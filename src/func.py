import eval
from node import Unit

def add(args: list[Unit]):
    resArr = []
    for arg in args:
        resUnit = eval.evaluate(arg)
        resArr.append(resUnit.value)
    result = Unit(sum(resArr))
    return result