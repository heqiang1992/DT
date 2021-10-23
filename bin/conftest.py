#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest,sys
from py._xmlgen import html
from lib.glo import _global_dict


# def pytest_configure(config):
#     config._metadata['auto_machine'] = '127.0.0.1 ~_~ '


# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("放在这里，后面可能要用")])


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
# cells.insert(2, html.th('Description'))
# cells.insert(3, html.th('Time', class_='sortable time', col='time'))
# cells.insert(1,html.th("Test_nodeid"))
# cells.pop()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     outcome = yield
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         if report.failed:
#             if "Logger" in _global_dict.keys():
#                 _global_dict["Logger"].warning(outcome.result.longreprtext)
#                 # _global_dict["Logger"].case_down()
#                 link = _global_dict["Logger"].file_path
#                 report.link = link
#         else:
#             if "Logger" in _global_dict.keys():
#                 link = _global_dict["Logger"].file_path
#                 report.link = link


# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     if report.failed:
#         cells.insert(3, html.td(
#             html.a("@__@$link here", href=report.link, target="_blank", style="color:blue;")))
#     else:
#         cells.insert(3, html.td(html.a("link here", href=report.link, target="_blank", style="color:blue;")))
#     cells.pop()


"""
fixture的优点：
命名方式灵活，不局限于 setup 和teardown 这几个命名
conftest.py 配置里可以实现数据共享，不需要 import 就能自动找到fixture
scope="module" 可以实现多个.py 跨文件共享前置
scope="session" 以实现多个.py 跨文件使用一个 session 来完成多个用例
"""

#创建前置
@pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
def hello():
    print("fixture初始化的参数列表")
"""
参数列表
scope：可以理解成fixture的作用域，默认：function，还有class、module、package、session四个【常用】
autouse：默认：False，需要用例手动调用该fixture；如果是True，所有作用域内的测试用例都会自动调用该fixture
name：默认：装饰器的名称，同一模块的fixture相互调用建议写个不同的name
注意
session的作用域：是整个测试会话，即开始执行pytest到结束测试

如何调用：
1.将fixture名称作为测试用例函数的输入参数
2.测试用例加上装饰器：@pytest.mark.usefixtures(fixture_name)
3.fixture设置autouse=True
（不是test开头，加了装饰器也不会执行fixture）

知识点
1.在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
2.可以叠加多个 @pytest.mark.usefixtures() ，先执行的放底层，后执行的放上层
3.可以传多个fixture参数，先执行的放前面，后执行的放后面
4.如果fixture有返回值，用 @pytest.mark.usefixtures() 是无法获取到返回值的，必须用传参的方式（方式一）
fixture的实例化顺序
较高 scope 范围的fixture（session）在较低 scope 范围的fixture（ function 、 class ）之前实例化【session > package > module > class > function】
具有相同作用域的fixture遵循测试函数中声明的顺序，并遵循fixture之间的依赖关系【在fixture_A里面依赖的fixture_B优先实例化，然后到fixture_A实例化】
自动使用（autouse=True）的fixture将在显式使用（传参或装饰器）的fixture之前实例化
"""
#调用示例
import pytest

# 调用方式一
@pytest.fixture
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例 1：登录之后其它动作 111")

# 调用方式二
@pytest.fixture
def login2():
    print("please输入账号，密码先登录")


@pytest.mark.usefixtures("login2", "login")
def test_s11():
    print("用例 11：登录之后其它动作 111")

# 调用方式三
@pytest.fixture(autouse=True)
def login3():
    print("====auto===")

"""
前面讲的，其实都是setup的操作，那么现在就来讲下teardown是怎么实现的
fixture之yield实现teardown
用fixture实现teardown并不是一个独立的函数，而是用 yield 关键字来开启teardown操作

yield注意事项:
如果yield前面的代码，即setup部分已经抛出异常了，则不会执行yield后面的teardown内容
如果测试用例抛出异常，yield后面的teardown内容还是会正常执行
"""
@pytest.fixture(scope="session")
def open():
    # 会话前置操作setup
    print("===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    # 会话后置操作teardown
    print("==关闭浏览器==")

"""
conftest.py
可以理解成一个专门存放fixture的配置文件
conftest.py配置fixture注意事项:
1.pytest会默认读取conftest.py里面的所有fixture
2.conftest.py 文件名称是固定的，不能改动
3.conftest.py只对同一个package下的所有测试用例生效
4.不同目录可以有自己的conftest.py，一个项目中可以有多个conftest.py
5.测试用例文件中不需要手动import conftest.py，pytest会自动查找
(最顶层的conftest，一般写全局的fixture)
"""


"""
选择性执行skip,skipif
"""
@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_case02():
    print("我是测试用例22222")
#跳过执行测试用例，有可选参数reason：跳过的原因，会在执行结果中打印
"""
知识点
@pytest.mark.skip 可以加在函数上，类上，类方法上
如果加在类上面，类里面的所有测试用例都不会执行
以上小案例都是针对：整个测试用例方法跳过执行，如果想在测试用例执行期间跳过不继续往下执行呢？(可以再用力函数中使用)
"""

"""
skipif
condition需要返回True才会跳过
"""
@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
class TestSkipIf(object):
    def test_function(self):
        print("不能在window上运行")


"""
跳过标记
可以将 pytest.mark.skip 和 pytest.mark.skipif 赋值给一个标记变量
在不同模块之间共享这个标记变量
若有多个模块的测试用例需要用到相同的 skip 或 skipif ，
可以用一个单独的文件去管理这些通用标记，然后适用于整个测试用例集
"""
skipmark = pytest.mark.skip(reason="不能在window上运行=====")
skipifmark = pytest.mark.skipif(sys.platform == 'win32', reason="不能在window上运行啦啦啦=====")


@skipmark
class TestSkip_Mark(object):

    @skipifmark
    def test_function(self):
        print("测试标记")
"""
pytest.importorskip( modname: str, minversion: Optional[str] = None, reason: Optional[str] = None )
作用：如果缺少某些导入，则跳过模块中的所有测试
参数列表:
modname：模块名
minversion：版本号
reasone：跳过原因，默认不给也行
"""
pexpect = pytest.importorskip("pexpect", minversion="0.3")

@pexpect
def test_import():
    print("test")