import json
import datetime
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def get_data(visit_url, params_str):
    req_str = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
               'page_num': '1',
               'page_size': '1000',
               # 'params': '{"cjsj__gte":"2023-01-01 00:00:00","cjsj__lte":"2023-08-01 00:00:00","ssjg__code":"a0105"}'
               # ssjg_id:0105 单个匹配   #ssjg__code__startswith:a0105查询a0105下面所有机构  sshd_id查询水道
               # hbscale_check() 航道尺度检查
               # gte大于等于 lte小于等于
               # 'params': '{"cjsj__gte":"2023-01-01 00:00:00","cjsj__lte":"2023-08-10 00:00:00","ssjg__code__startswith":"a0105"}'
               # wypy_Judege() 位移漂移检查
               # 'params': '{"hb__ssjg__code__startswith":"a0105"}'
               # adjust_dist() 调标距离检查
               # 'params': '{"cjsj__gte":"2023-01-01 00:00:00","cjsj__lte":"2023-08-01 00:00:00","hb__ssjg__code__startswith":"a0105"}'
               # 'params': '{"cjsj__gte":"2023-07-01 00:00:00","cjsj__lte":"2023-08-01 00:00:00","ssjg__code__startswith":"a0105"}'
               # swz_data 水位站数据
               # 'params': '{"cjsj__gte":"2023-08-14 00:00:00","cjsj__lte":"2023-08-14 10:00:00","swz__ssjg__code__startswith":"a0105"}'
               'params': params_str
               }
    # url_str = 'http://172.18.128.153/api/fw/hb/hbjcxx/'
    result = requests.post(url=visit_url, data=req_str, verify=False).json()
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    return result
