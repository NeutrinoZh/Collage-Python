import mymath
import pytest
import sys

def test_add_integers():
    result = mymath.add(1, 2)
    assert result == 3
    
def test_add_floats():
    result = mymath.add(10.5, 2)
    assert result == 12.5
    

@pytest.mark.xfail()
def test_add_strings():
    result = mymath.add('abc', 'def')
    assert result == 'abcde'

@pytest.mark.skip()
def test_failed_for_not_win32_systems():
    assert False

@pytest.mark.skipif(sys.platform != "win64", reason="requires windows 64bit")
def test_skipped_for_not_win64_systems():
    assert False