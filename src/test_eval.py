import eval
import parser
import unittest
from node import Unit

def parseAndEval(s: str) -> str:
    ctx: dict[str, Unit] = {}
    t = parser.parser(s)
    result = eval.evaluate(t, ctx)
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

def test_eval_c13():
    assert parseAndEval('(- (+ (+ 2 1) 4) (+ 5 6))') == '-4'

def test_eval_c14():
    assert parseAndEval('(+ 1 2 3)') == '6'

def test_seq_c1():
    assert parseAndEval('(seq (+ 1 2) (+ 3 4) (+ 5 6))') == '11'

def test_val_c1():
    assert parseAndEval('( seq ( val x 1) ( plus x 3 ) )') == '4'

def test_val_c2():
    assert parseAndEval('( seq (val a 1) a)') == '1' 

def test_val_c3():
    assert parseAndEval('( seq (val a "ab") a )') == '"ab"'

def test_len_c1():
    assert parseAndEval('(len "ab")') == '2'

def test_con_c1():
    assert parseAndEval('(con "ab" "cd")') == '"abcd"'

  
