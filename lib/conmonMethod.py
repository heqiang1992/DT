#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import time


def generate_time_postfix():
    TIMESTAMP = datetime.datetime.fromtimestamp(time.time())
    DATE = datetime.datetime.strftime(TIMESTAMP, "%Y_%m_%d_%H_%M_%S")
    DATE = str(DATE).replace(" ", "_")
    return DATE