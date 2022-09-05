import func
from node import Unit





def evaluate(n: Unit, ctx: dict[str, Unit]) -> Unit:
    if(n == None):
        return Unit(None)
    result = None
    if(n.value in ['plus', '+']):
        result = func.addtion(n.args, ctx)
    elif(n.value in ['minus', '-']):
        result = func.subtraction(n.args, ctx)
    elif(n.value in ['multiply', '*', 'x']):
        result = func.multiplacation(n.args, ctx)
    elif(n.value in ['divide', '/']):
        result = func.divition(n.args, ctx)
    elif(n.value in ['seq']):
        result = func.sequence(n.args, ctx)
    elif(n.value in ['val']):
        result = func.define(n.args, ctx)
    else:
        if(n.isNumber() == True):
            result = Unit(int(n.value))
        elif(n.isString()):
            return n
        else:
            token = n.value
            if(token in ctx):
                return ctx[token]
            else:
                raise TypeError("Variable "+ token +" Not Found!")
    #print(result.value)
    return result
