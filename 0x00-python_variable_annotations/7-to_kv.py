#!/usr/bin/env python3
'''Python - Variable annotation'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    '''Pytho annotation'''
    value = (k, float(v * v))
    return value
