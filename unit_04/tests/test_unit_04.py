"""

"""
import pytest


def test_stack():
    stack = []
    stack.append(0)
    stack.append(1)

    assert stack.pop() == 1
    assert stack.pop() == 0


def test_emptiness():
    stack = []
    assert not stack
    stack.append(0)
    assert bool(stack)

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()


