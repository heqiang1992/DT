#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest


def func(x):
    return x + 1


def test_func1():
    assert func(4) == 5  # 成功示例


def test_func2():
    a = "here"
    assert func(3) == 5  # 失败示例


if __name__ == "__main__":
    pytest.main()


