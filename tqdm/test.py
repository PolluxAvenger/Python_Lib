# coding=utf-8
# 进一步文档地址：https://pypi.python.org/pypi/tqdm

import time
import tqdm

for i in tqdm.tqdm(range(100)):
    time.sleep(1)
