from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,5)==9

def test_sub():
    assert sub(7,2)==5
    assert sub(8,4)==4