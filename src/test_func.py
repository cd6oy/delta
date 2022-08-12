from node import Unit
import func

def test_add_c1():
    assert func.add([Unit(2), Unit(3)]).toString() == '5'
def test_add_c2():
    assert func.add([Unit(1), Unit(3), Unit(2), Unit(5)]).toString() == '11'