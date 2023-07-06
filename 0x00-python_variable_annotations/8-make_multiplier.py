#!/usr/bin/env python3
'''Python - Variable annotation'''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Python - annotation'''
    def muli(a: float) -> float:
        return (a * multiplier)
    return muli
