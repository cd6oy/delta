from ast import Global


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
    def toString(self):
        if self.left == None and self.right == None:
            r = str(self.value)
        else:
            r = '('
            r = r+ str(self.value)
            r = r+ ', '
            if self.left != None:  
                r = r+str(self.left.toString())
            else:
                r = r+ str('')
            r = r+', '
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

def parse(input: str) -> Tree:
    i = 0
    n = None
    while i < len(input):
        p = input[i]
        if(p == '('):
            i = i+1
            p = input[i]
            n = Node(p)
        elif(p == ')'):
            return Tree(n)
            
        elif(p == ','):
            None
        else:
            if(n.left == None):
                n.left = Node(p)
            elif(n.right == None):
                n.right = Node(p)
        i = i+1


    return Tree(n)

#t = makeTree()
#print(t.toString())

t = parse("(a,b,c)")
print(str(t.toString()))
t1 = parse("(a)")
print(str(t1.toString()))
t2 = parse("a")
print(str(t2.toString()))
#print(makeTree())
#print(t.value)