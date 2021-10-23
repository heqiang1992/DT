#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest


@pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
def beforetest():
    print("fixture: beforetest setup#$%^&*()")


@pytest.mark.usefixtures("beforetest")
def test_hello():
    print("hello")