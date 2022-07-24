import tokenizer

def test_tokenizer_c1():
    assert tokenizer.tokenizer("( ab c d)", 0) == 1
def test_tokenizer_c2():
    assert tokenizer.tokenizer("( ab c d)", 1) == 2
def test_tokenizer_c3():
    assert tokenizer.tokenizer("( ab c d)", 2) == 4
def test_tokenizer_c4():
    assert tokenizer.tokenizer("( ab c d)", 4) == 5
def test_tokenizer_c5():
    assert tokenizer.tokenizer("( ab c d)", 6) == 7
def test_tokenizer_c6():
    assert tokenizer.tokenizer("( ab c d)", 7) == 8
def test_tokenizer_c7():
    assert tokenizer.tokenizer("( ab c d)", 8) == 9