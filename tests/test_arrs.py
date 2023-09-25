from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([10, 20, 30], 0, "test") == 10
    assert arrs.get([1, 2, 3, 4], 3, "test") == 4
    assert arrs.get([1, 2, 3], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    assert arrs.get([1, "two", 3.0], 2) == 3.0

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 0) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3) == [3, 4, 5]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice([], None, None) == []
    assert arrs.get([1, "two", 3.0], 2) == 3.0
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
