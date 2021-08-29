import pytest
from npspy import InvalidAnswerError, categorize, calculate


def test_categorize_negative():
    with pytest.raises(InvalidAnswerError):
        categorize(-1)


def test_categorize_0():
    assert categorize(0) == "detractor"


def test_categorize_6():
    assert categorize(6) == "detractor"


def test_categorize_7():
    assert categorize(7) == "passive"


def test_categorize_8():
    assert categorize(8) == "passive"


def test_categorize_9():
    assert categorize(9) == "promoter"


def test_categorize_10():
    assert categorize(10) == "promoter"


def test_categorize_more_than_10():
    with pytest.raises(InvalidAnswerError):
        categorize(11)


def test_calculate_0():
    assert calculate([0, 9]) == 0


def test_calculate_33():
    assert calculate([7, 8, 9]) == 1 / 3 * 100


def test_calculate_100():
    assert calculate([9, 10]) == 100
