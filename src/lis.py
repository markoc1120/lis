"""Computing increasing substrings."""

# The Any annotations here is saying that we will accept any type.
# They *should* be comparable, and it *is* possible to make such
# an annotation, but it is tricky, and I don't want to confuse you
# more than strictly necessary.
from typing import Sequence, Any


def is_increasing(x: Sequence[Any]) -> bool:
    """
    Determine if x is an increasing sequence.

    >>> is_increasing([])
    True
    >>> is_increasing([42])
    True
    >>> is_increasing([1, 4, 6])
    True
    >>> is_increasing("abc")
    True
    >>> is_increasing("cba")
    False
    """
    for i in range(len(x) - 1):
        if not x[i] < x[i+1]:
            return False
    return True


def substring_length(substring: tuple[int, int]) -> int:
    """Give us the length of a substring, represented as a pair."""
    return substring[1] - substring[0]


def longest_increasing_substring(x: Sequence[Any]) -> tuple[int, int]:
    """
    Locate the (leftmost) longest increasing substring.

    If x[i:j] is the longest increasing substring, then return the pair (i,j).

    >>> longest_increasing_substring('abcabc')
    (0, 3)
    >>> longest_increasing_substring('ababc')
    (2, 5)
    >>> longest_increasing_substring([12, 45, 32, 65, 78, 23, 35, 45, 57])
    (5, 9)
    """
    # The leftmost empty string is our first best bet
    best = (0, 0)
    for i in range(len(x)):
        for j in range(i+1, len(x)+1):
            if is_increasing(x[i:j]) and \
                    substring_length((i, j)) > substring_length(best):
                best = (i, j)
    return best


def fast_lis(x: Sequence[Any]) -> tuple[int, int]:
    """
    Locate the (leftmost) longest increasing substring.

    If x[i:j] is the longest increasing substring, then return the pair (i,j).

    >>> fast_lis('abcabc')
    (0, 3)
    >>> fast_lis('ababc')
    (2, 5)
    >>> fast_lis([12, 45, 32, 65, 78, 23, 35, 45, 57])
    (5, 9)
    """
    # With this solution, it is easier to deal with the empty
    # sequence as a special case up front.
    if not x:
        return (0, 0)

    # The leftmost empty string is our first best bet
    best = (0, 0)
    cur_start = 0
    for i in range(1, len(x)):
        if not x[i-1] < x[i]:
            # break current stretch
            if substring_length((cur_start, i)) > substring_length(best):
                best = (cur_start, i)
            cur_start = i  # start new stretch

    # Special case at the end, where we need to check if adding the last
    # character can increase the current length
    if substring_length((cur_start, len(x))) > substring_length(best):
        best = (cur_start, len(x))

    return best
