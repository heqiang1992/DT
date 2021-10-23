#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest, sys

"""
pytest 可以支持自定义标记，自定义标记可以把一个 web 项目划分多个模块，然后指定模块名称执行
譬如我可以标明哪些用例是window下执行的，哪些用例是mac下执行的，在运行代码时候指定mark即可
"""

import pytest


@pytest.mark.weibo
def test_weibo():
    print("测试微博")


@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")
"""
执行：
pytest -s -m weibo 08_mark.py
如果不想标记weibo的用例，我们直接取反即可：
pytest -s -m "not weibo" 08_mark.py
如果想执行多个自定义标记的用例：
pytest -s -m "toutiao or weibo" 08_mark.py
"""

"""
参数化
pytest允许在多个级别启用测试参数化：
1. pytest.fixture() 允许fixture有参数化功能（后面讲解）
2. @pytest.mark.parametrize 允许在测试函数或类中定义多组参数和fixtures
3. pytest_generate_tests 允许定义自定义参数化方案或扩展（拓展）
"""
#举例，下面是未参数化的代码
def test_1():
    assert 3 + 5 == 9

def test_2():
    assert 2 + 4 == 6

#利用参数化优化之后的代码：
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    print(f"测试数据{test_input},期望结果{expected}")
    assert eval(test_input) == expected

#可以看到，只有一条用例，但是利用参数化输入三组不同的测试数据和期望结果，最终执行的测试用例数=3，可以节省很多代码
# 实际Web UI自动化中的开发场景，比如是一个登录框
# 你肯定需要测试账号空、密码空、账号密码都为空、账号不存在、密码错误、账号密码正确等情况
# 所以我们可以只写一条登录测试用例，然后把多组测试数据和期望结果参数化，节省很多代码量

#参数讲解
def parametrize(self,argnames, argvalues, indirect=False, ids=None, scope=None):
    pass
"""
argnames:
源码解析：a comma-separated string denoting one or more argument names, or a list/tuple of argument strings.
含义：参数名字
格式：字符串"arg1,arg2,arg3"【需要用逗号分隔】

argvalues:
含义：参数值列表
格式：必须是列表，如：[ val1,val2,val3 ]
如果只有一个参数，里面则是值的列表如：@pytest.mark.parametrize("username", ["yy", "yy2", "yy3"])
如果有多个参数例，则需要用元组来存放值，一个元组对应一组参数的值，如：@pytest.mark.parametrize("name,pwd", [("yy1", "123"), ("yy2", "123"), ("yy3", "123")])

ids
含义：用例的ID
格式：传一个字符串列表
作用：可以标识每一个测试用例，自定义测试数据结果的显示，为了增加可读性
强调：ids的长度需要与测试数据列表的长度一致

indirect
作用：如果设置成True，则把传进来的参数当函数执行，而不是一个参数（后面详讲）
"""


"""
为了提高复用性，我们在写测试用例的时候，会用到不同的fixture，比如：最常见的登录操作，大部分的用例的前置条件都是登录
假设不同的用例想登录不同的测试账号，那么登录fixture就不能把账号写死，需要通过传参的方式来完成登录操作
"""
import pytest


@pytest.fixture()
def login(request):
    name = request.param
    print(f"== 账号是：{name} ==")
    return name

data = ["pyy1", "polo"]
ids = [f"login_test_name is:{name}" for name in data]

@pytest.mark.parametrize("login", data, ids=ids, indirect=True)
def test_name(login):
    print(f" 测试用例的登录账号是：{login} ")
"""
知识点
添加  indirect=True  参数是为了把 login 当成一个函数去执行，而不是一个参数，并且将data当做参数传入函数
def test_name(login) ，这里的login是获取fixture返回的值
"""