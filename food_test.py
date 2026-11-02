import pytest

from food import total


@pytest.mark.parametrize(
    ("p", "d", "out"),
    [(100, 10, 90), (0, 0, 0), (100, 0, 100), (100, 100, 0)],
)
def test_total(p, d, out):
    assert total(p, d) == out


@pytest.mark.parametrize("p, d", [(-1, 10), (100, -1), (100, 101)])
def test_bad(p, d):
    with pytest.raises(ValueError):
        total(p, d)

