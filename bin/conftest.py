#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py._xmlgen import html
from lib.glo import _global_dict


def pytest_configure(config):
    config._metadata['auto_machine'] = '127.0.0.1 ~_~ '


# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("放在这里，后面可能要用")])


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
# cells.insert(2, html.th('Description'))
# cells.insert(3, html.th('Time', class_='sortable time', col='time'))
# cells.insert(1,html.th("Test_nodeid"))
# cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        if report.failed:
            if "Logger" in _global_dict.keys():
                _global_dict["Logger"].warning(outcome.result.longreprtext)
                # _global_dict["Logger"].case_down()
                link = _global_dict["Logger"].file_path
                report.link = link
        else:
            if "Logger" in _global_dict.keys():
                link = _global_dict["Logger"].file_path
                report.link = link


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    if report.failed:
        cells.insert(3, html.td(
            html.a("@__@$link here", href=report.link, target="_blank", style="color:blue;")))
    else:
        cells.insert(3, html.td(html.a("link here", href=report.link, target="_blank", style="color:blue;")))
    cells.pop()



