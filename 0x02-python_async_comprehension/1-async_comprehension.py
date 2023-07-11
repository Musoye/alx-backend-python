#!/usr/bin/env python3
'''Asynchronous Comprehension as in PEP 525'''


import asyncio
from typing import List
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''The asynchronous generator function'''
    return [val async for val in async_generator()]
