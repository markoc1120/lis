"""Testing longest increasing substring."""

import random
from lis import (
    longest_increasing_substring,
    is_increasing
)


def test_special_cases() -> None:
    """Check some special cases that might go wrong."""
    assert longest_increasing_substring('') == (0, 0)
    assert longest_increasing_substring('x') == (0, 1)


def test_we_get_increasing() -> None:
    """Test that the substring we get back is increasing."""
    for _ in range(10):
        x = random.sample(range(100), random.randint(1, 10))
        i, j = longest_increasing_substring(x)
        assert is_increasing(x[i:j])

# Without giving you the solution, I cannot check if you get the
# longest sub-string... I would need code for finding it...
