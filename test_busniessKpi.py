import busniessKpi as bKpi
import pytest as pyt

data01 = [5,5]
data02 = [5,5,5,6,6,6,6]

@pyt.mark.parametrize("input1, intut2, input3, expected", [(data01, 0.05, 100, 100),(data02, 0.05, 100, 103)])

def sagMoin():
    print("Moin!!!")

def test_expo(input1, intut2, input3, expected):
    result = bKpi.expo(input1, intut2, input3)
    assert result == expected