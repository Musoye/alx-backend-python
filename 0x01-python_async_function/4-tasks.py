#!/usr/bin/env python3
'''The aync operation in python'''


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''This is an async function'''
    listed = []
    for _ in range(n):
        value = task_wait_random(max_delay)
        listed.append(value)
    val = [await r for r in asyncio.as_completed(listed)]
    return val
