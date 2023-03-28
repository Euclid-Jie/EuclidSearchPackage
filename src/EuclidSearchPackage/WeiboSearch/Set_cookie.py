# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 12:12
# @Author  : Euclid-Jie
# @File    : Set_cookie.py

import os
import shutil
from glob import glob


def Set_cookie(cookieFilePath):
    if not os.path.isfile(cookieFilePath):
        print("%s not exist!" % cookieFilePath)
    else:
        current_dir = os.path.abspath(os.path.dirname(__file__))
        shutil.copy(cookieFilePath, os.path.join(current_dir + '\\cookie.txt'))  # 复制文件
        print("set cookie success.")
