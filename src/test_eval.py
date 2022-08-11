import eval
import parser
import unittest

def parseAndEval(s: str) -> str:
    t = parser.parser(s)
    result = eval.evaluate(t)
    return result.toString()

class testEval(unittest.TestCase):
  
    # Returns true if 1 + '1' raises a TypeError
    def test_eval_c1(self):
        with self.assertRaises(Exception) as context:
            parseAndEval('(+ a 3)')
        # assert context.exception == ''
def test_eval_c2():
    assert parseAndEval('(+ 3 2)') == '5'

def test_eval_c3():
    assert parseAndEval('(plus 3 2)') == '5'

def test_eval_c4():
    assert parseAndEval('(minus 3 2)') == '1'

def test_eval_c5():
    assert parseAndEval('(- 3 2)') == '1'

def test_eval_c6():
    assert parseAndEval('(multiply 3 2)') == '6'

def test_eval_c7():
    assert parseAndEval('(* 3 2)') == '6'

def test_eval_c8():
    assert parseAndEval('(x 3 2)') == '6'

def test_eval_c9():
    assert parseAndEval('(divide 6 3)') == '2'

def test_eval_c10():
    assert parseAndEval('(/ 6 3)') == '2'

def test_eval_c11():
    assert parseAndEval('(+ (- 5 3) 4)') == '6'

def test_eval_c12():
    assert parseAndEval('(- (+ (+ 2 1) 4) (+ 1 4))') == '2'

def test_eval_c12():
    assert parseAndEval('(- (+ (+ 2 1) 4) (+ 5 6))') == '-4'

def test_eval_c13():
    assert parseAndEval('(+ 1 2 3)') == '6'
  
#if __name__ == '__main__': 
 #   unittest.main()