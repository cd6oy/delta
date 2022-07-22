import makeTree

def parseWithTest(testcase: str) -> str:
    t = makeTree.parse(testcase)
    return t.toString()
    #print(str(testcase + "=>" + t.toString()))
# example = makeTree.parse()

def test_parse_c1():
    assert parseWithTest('(a b c)') == '(a b c)'

def test_parse_c2():
    assert parseWithTest('( a   )') == 'a'
def test_parse_c3():
    assert parseWithTest('     a   ') == 'a'
def test_parse_c4():
    assert parseWithTest('(   a b  c                     )') == '(a b c)'
def test_parse_c5():
    assert parseWithTest('( abc             d   e)') == '(abc d e)'
def test_parse_c6():
    assert parseWithTest('( abc       def  ghi   )') == '(abc def ghi)'

def test_tokenizer_c1():
    assert makeTree.tokenizer("( ab c d)", 0) == 1
def test_tokenizer_c2():
    assert makeTree.tokenizer("( ab c d)", 1) == 2
def test_tokenizer_c3():
    assert makeTree.tokenizer("( ab c d)", 2) == 4
def test_tokenizer_c4():
    assert makeTree.tokenizer("( ab c d)", 4) == 5
def test_tokenizer_c5():
    assert makeTree.tokenizer("( ab c d)", 6) == 7
def test_tokenizer_c6():
    assert makeTree.tokenizer("( ab c d)", 7) == 8
def test_tokenizer_c7():
    assert makeTree.tokenizer("( ab c d)", 8) == 9









