from bs4 import BeautifulSoup
import pandas as pd
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import Login
#访问分中心
def visit_host(url):
    cookies = {
        'chang_session': Login.get_fzx_Session(),
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Referer': 'https://172.18.128.153/vadmin/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    return response
#访问主中心
def visit_zzx_host(url):
    cookies = {
        'chang_session': Login.get_zzx_Session(),
    }
    headers = {'Accept': 'application/json, text/plain, */*',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Cache-Control': 'no-cache',
              'Connection': 'keep-alive',
              'Content-Length': '170',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': '172.18.101.51',
              'Origin': 'http://172.18.101.51',
              'Pragma': 'no-cache',
              'Referer': 'http://172.18.101.51/vadmin/',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
              }
    Data={'hide_data':'{"update_content":1}',
          'event_data':'{"name":""}'}
    response = requests.post(url, headers=headers, cookies=cookies,data=Data)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    return response





