#!/usr/bin/env python3
'''The types of the elements of the input are not kno'''


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Python - Variable Annotation'''
    if lst:
        return lst[0]
    else:
        return None
