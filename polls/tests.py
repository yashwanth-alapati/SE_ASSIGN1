#from django.test import TestCase

# Create your tests here.

import pytest
from .utils import add_numbers

# Use pytest's built-in functions for testing
def test_add_two_positive_numbers():
    result = add_numbers(3, 5)
    assert result == 8

def test_add_negative_number():
    result = add_numbers(-1, 1)
    assert result == 0

def test_add_zero():
    result = add_numbers(0, 0)
    assert result == 0
