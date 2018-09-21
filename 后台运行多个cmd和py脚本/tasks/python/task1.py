# encoding: utf-8
"""
@File: task1.python

Created on 2018/9/21 9:50

@author: weiyd

Description:
"""
import time

while True:
    time_stamp = int(time.time())
    format_string = "%Y-%m-%d %H:%M:%S"
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    print(str_date)
