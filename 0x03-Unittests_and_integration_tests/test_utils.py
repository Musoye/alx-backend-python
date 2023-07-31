#!/usr/bin/python3
"""Test a utils function"""


import unittest
from unittest.mock import patch
from parameterized import parameterized # type: ignore
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """A Nested Map test case"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result: int) -> None:
        """A Test case for nested map"""
        self.assertEqual(access_nested_map(nested_map, path), result)
