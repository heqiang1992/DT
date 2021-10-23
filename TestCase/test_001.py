#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest


def func(x):
    return x + 1


def test_func1():
    print("001-func1")
    assert func(4) == 5  # 成功示例


def test_func2():
    print("001-func2")
    assert func(3) == 5  # 失败示例


if __name__ == "__main__":
    pytest.main()


