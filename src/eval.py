import func
from node import Unit




def evaluate(n: Unit) -> Unit:
    if(n == None):
        return Unit(None)
    result = None
    if(n.value in ['plus', '+']):
        result = func.addtion(n.args)
    elif(n.value in ['minus', '-']):
        result = func.subtraction(n.args)
    elif(n.value in ['multiply', '*', 'x']):
        result = func.multiplacation(n.args)
    elif(n.value in ['divide', '/']):
        result = func.divition(n.args)
    elif(n.value in ['seq']):
        l = []
        for arg in n.args:
            lu = evaluate(arg)
            l.append(lu)
        result = l[len(l)-1]
    else:
        if(str(n.value).isnumeric() == False):
            raise TypeError("Only integers are allowed!")

        else:
            result = Unit(int(n.value))
    #print(result.value)
    return result
