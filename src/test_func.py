from node import Unit
import func

def test_addtion_c1():
    assert func.addtion([Unit(2), Unit(3)]).toString() == '5'
def test_addtion_c2():
    assert func.addtion([Unit(1), Unit(3), Unit(2), Unit(5)]).toString() == '11'
def test_subtraction_c1():
    assert func.subtraction([Unit(3), Unit(1)]).toString() == '2'
def test_multiplacation_c1():
    assert func.multiplacation([Unit(2), Unit(3), Unit(1)]).toString() == '6'
def test_divition_c1():
    assert func.divition([Unit(9), Unit(3)]).toString() == '3'