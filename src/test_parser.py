import parser

def parseWithTest(testcase: str) -> str:
    t = parser.parser(testcase)
    assert t != None
    return t.toString()
    #print(str(testcase + "=>" + t.toString()))
# example = makeTree.parse()

def test_parse_c1():
    assert parseWithTest('(a b c)') == '( a b c )'

def test_parse_c2():
    assert parseWithTest('( a   )') == 'a'
def test_parse_c3():
    assert parseWithTest('     a   ') == 'a'
def test_parse_c4():
    assert parseWithTest('(   a b  c                     )') == '( a b c )'
def test_parse_c5():
    assert parseWithTest('( abc             d   e)') == '( abc d e )'
def test_parse_c6():
    assert parseWithTest('( abc       def  ghi   )') == '( abc def ghi )'
def test_parse_c7():
    assert parseWithTest('( abc       (d e f)  ghi   )') == '( abc ( d e f ) ghi )'
def test_parse_c8():
    assert parseWithTest('(+ 1 2 3)') == '( + 1 2 3 )'
def test_parse_str_c1():
    assert parseWithTest('("a b c")') == '( "a b c" )'
def test_parse_str_c2():
    assert parseWithTest(' "Larry" ') == '"Larry"'












