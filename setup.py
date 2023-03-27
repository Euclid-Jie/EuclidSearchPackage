# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 22:22
# @Author  : Euclid-Jie
# @File    : setup.py.py
from setuptools import setup, find_packages

setup(
    name='EuclidSearchPackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'bs4',
        'lxml',
        'selenium',
        'pymongo',
        'tqdm',
        'requests_html',
    ],
    author='Euclid-Jie',
    author_email='Ouweijie123@outlook.com',
    description='a package for search data from weibo, zhihu, guba and etc.',
    url='https://github.com/Euclid-Jie/EuclidSearchPackage',
)
