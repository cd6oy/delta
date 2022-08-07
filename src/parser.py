from tokenizer import tokenizer
from node import Unit

def parseTree(input: str, startPos) -> Unit and int:
    i = startPos
    n = None
    while i < len(input):
        end = tokenizer(input, i)
        word = input[i: end]
        if(word == '('):
            if(n == None):
                n = Unit(None)
            else:
                result = parseTree(input, i)
                unit = result[0]
                i = result[1]
                #print(result[1])
                n.args.append(unit)
                end = i+1
        elif(word == ')'):
            return n, i
        elif(word == ' '):
            None
    
        else:
            if(n == None):
                n = Unit(word)
            elif(n.value == None):
                n.value = word
            else:
                #print(Unit(word).value)
                n.args.append(Unit(word))
        i = end
    return n, i

def parser(testcase: str):
    return parseTree(testcase, 0)[0]