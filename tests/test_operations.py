from src.math_operation import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 1.5) == 4.0

def test_subtract():
    assert sub(5, 3) == 2
    assert sub(0, 1) == -1
    assert sub(-1, -1) == 0
    assert sub(2.5, 1.5) == 1.0
