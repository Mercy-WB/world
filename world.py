# -*- coding: utf-8 -*-
"""
    世界。

    Log:
    2020年4月5日 16:48:08 创建
"""

__author__ = 'Mercy'
__version__ = '0.1'

from dao import Substance, Way


def motion():
    """
        运动
    :return:
    """
    way = Way()
    sub = Substance()
    return True


if __name__ == '__main__':
    while motion():
        pass
