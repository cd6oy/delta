import eval
import parser

def parseAndEval(s: str) -> str:
    t = parser.parse(s)
    result = eval.evaluate(t)
    return result.toString()


def test_eval_c1():
    assert parseAndEval('(plus 3 2)') == '5'

def test_eval_c2():
    assert parseAndEval('(+ 3 2)') == '5'

def test_eval_c3():
    assert parseAndEval('(minus 3 2)') == '1'

def test_eval_c4():
    assert parseAndEval('(- 3 2)') == '1'

def test_eval_c5():
    assert parseAndEval('(multiply 3 2)') == '6'

def test_eval_c6():
    assert parseAndEval('(* 3 2)') == '6'

def test_eval_c7():
    assert parseAndEval('(x 3 2)') == '6'

def test_eval_c8():
    assert parseAndEval('(divide 6 3)') == '2'

def test_eval_c9():
    assert parseAndEval('(/ 6 3)') == '2'