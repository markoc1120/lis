# Longest increasing substring

Given a sequence `x` over whatever type you can think of that has an order to it (i.e. we can compare if one element is smaller than another), we can define *increasing substrings* as a slice `x[i:j]` where each element is smaller than the following. Despite the name sub*string*, it doesn't have to be an actual string. It is just the anme for this kind of sub-sequence, where the elements are consecutive.

The function below will check if an entire list is increasing. You could call it as `is_increasing(x)`. If you wanted to know if a sub-string `x[i:j]` is increasing, you could just as well as `is_increasing(x[i:j])`.


```python
def is_increasing(x: Sequence[Any]) -> bool:
    """
    Determine if x is an increasing sequence.
    """
    for i in range(len(x) - 1):
        if not x[i] < x[i+1]:
            return False
    return True
```

We want a function that gives us the longest increasing substring of any given sequence `x`. This could be the entire sequence, of course, if the full sequence is increasing. It is possible that two inreasing substrings have the same length, but in that case we want the left-most. (It isn't often that we care which of a set of ties we want, but there are such cases, and I have decided that I want the left-most).

In applications with very long strings, copying out a substring can be expensive. However, we have the same information if we have `x[i:j]` or `(x,i,j)`, so if we already know `x`, then we can represent a substring simply using the indices `i` and `j`. So our function should return that.

With this representation, you can get the length of a substring like this:

```python
def substring_length(substring: tuple[int, int]) -> int:
    """Give us the length of a substring, represented as a pair."""
    return substring[1] - substring[0]
```

