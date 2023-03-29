# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 21:36
# @Author  : Euclid-Jie
# @File    : Get_single_weibo_data_async.py

import json
import os
import requests
from ..Utils import Set_header


def Get_single_weibo_data_async(mblogid):
    """
    get single weibo's data by weibo_url, just like https://weibo.com/1310272120/MrOtA75Fd
    which can get by using Get_item_url_list.py

    in fact get https://weibo.com/ajax/statuses/show?id=MrOtA75Fd
    con help to simplify works

    Attention: If need full content text, another get is needed https://weibo.com/ajax/statuses/longtext?id=MrOtA75Fd

    data contains:
        text: weibo content with some html
        text_raw: weibo content
        region_name: province

        attitudes_count = data['attitudes_count']
        comments_count = data['comments_count']
        reposts_count = data['reposts_count']

        mid: a id correspond to this weibo
        created_at: the time created this weibo
        source: the specific device information, just like "Phone 14 Pro"
        screen_name: the user who created this weibo
        ......
    """
    URL = 'https://weibo.com/ajax/statuses/show?id={}'.format(mblogid)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    header = Set_header(os.path.join(current_dir, 'cookie.txt'))
    response = requests.get(URL, headers=header, timeout=60)  # 使用request获取网页
    html = response.content.decode('utf-8', 'ignore')  # 将网页源码转换格式为html
    data_json = json.loads(html, strict=False)
    return data_json


if __name__ == '__main__':
    data = Get_single_weibo_data_async(mblogid='MrOtA75Fd')
    part_data = {
        'time': data['created_at'],
        'mid': data['mid'],
        'nick_name': data['user']['screen_name'],
        'attitudes_count': data['attitudes_count'],
        'comments_count': data['comments_count'],
        'reposts_count': data['reposts_count'],
        'text': data['text'],
        'text_raw': data['text_raw']
    }
    print(part_data)
