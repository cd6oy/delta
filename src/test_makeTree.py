import makeTree

def parseWithTest(testcase: str) -> str:
    t = makeTree.parse(testcase)
    return t.toString()
    #print(str(testcase + "=>" + t.toString()))
# example = makeTree.parse()

def test_parse_c1():
    assert parseWithTest('(a,b,c)') == '(a, b, c)'
def test_parse_c2():
    assert parseWithTest('(a)') == 'a'
def test_parse_c3():
    assert parseWithTest('a') == [('a')]
def test_parse_c4():
    assert parseWithTest('(abc)') == [('abc')]
def test_parse_c5():
    assert parseWithTest('(abc,d,e)') == [('(abc,d,e)')]
def test_parse_c6():
    assert parseWithTest('(abc,def,ghi)') == [('(abc,def,ghi)')] 