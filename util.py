# coding:utf8
import re


def filter_items(regex, items):
    """使用正则过滤列表"""
    regex_pattern = re.compile(regex)
    items = [x for x in items if regex_pattern.match(x)]
    return items
