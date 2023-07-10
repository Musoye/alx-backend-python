#!/usr/bin/env python3
'''The aync operation in python'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''This is an async function'''
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
