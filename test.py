from asyncio import base_events
from dataclasses import dataclass, fields
from importlib.metadata import requires
from typing import Optional, Any


class Master:
    def __new__(cls):
        print('Master new')
        print(cls.__bases__)
        return object.__new__(cls)

    def __init__(self):
        print('Master init')


class Base(Master):
    def __init__(self):
        print('Base init')


class C1(Base):
    # def __new__(cls):
    #     print('C1 new')
    #     return object.__new__(cls)

    def __init__(self):
        print('C1 init')


C1()
