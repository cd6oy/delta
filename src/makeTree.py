


class Node:
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None
    def toString(self):
        if self.left == None and self.right == None:
            r = str(self.value)
        else:
            r = '('
            r = r+ str(self.value)
            r = r+ ' '
            if self.left != None:  
                r = r+str(self.left.toString())
            else:
                r = r+ str('')
            r = r+' '
            if self.right != None:
                r = r+str(self.right.toString())
            else:
                r = r+str('')
            r = r+')'
        return r


class Tree:
    def __init__(self, value: Node):
        self.root = value
    def toString(self):
        r = self.root.toString()
        return r
    def print(self):
        string = []
        p = self.root
        q = self.root
        while p != None and q != None:
            if q != p:
                string.append(str(p.value))
                string.append(str(q.value))
                p = p.left
                q = q.right
            else:
                string.append(str(p.value))
                p = p.left
                q = q.right
        ', '.join(string)
        return string.value


def makeTree():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = None
    t = Tree(n1)
    return t

def makeSimpleTree():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    tr = Tree(n1)
    return tr


def tokenizer(input: str, start):
    p = start
    while p != len(input):
        if(input[p] in ['(', ')', ' '] and p == start):
            return p+1
        elif(input[p] in ['(', ')', ' '] and p != start):
            print(p)
            return p
        else:
            p += 1
    


def parse(input: str) -> Tree:
    i = 0
    n = None
    while i < len(input):
        end = tokenizer(input, i)
        word = input[i: end]
        if(word == '('):
            #i = i+1
            word = input[i: end]
            #print('WORD:' + word)
            #print('INPUT[I: END]: ' + input[i: end])
            n = Node(None)
        #elif(i+1 == None):
         #   return p
        elif(word == ')'):
            return Tree(n)
        elif(word == ' '):
            None
    
        else:
            if(n == None):
                n = Node(word)
            elif(n.value == None):
                n.value = word
            #elif(input[i+1] ! ','):
             #   list = list + p
            elif(n.left == None):
                n.left = Node(word)
            elif(n.right == None):
                n.right = Node(word)
        i = end


    return Tree(n)
