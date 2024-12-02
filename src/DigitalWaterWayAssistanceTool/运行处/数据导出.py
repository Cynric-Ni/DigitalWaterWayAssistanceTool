import requests
import os
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
import ddddocr

class 数据导出:
    @staticmethod
    def 创建多层文件夹(路径):
        # 判断路径是否存在
        是否存在 = os.path.exists(路径)
        if not 是否存在:
            # 如果不存在，则创建目录（多层）
            os.makedirs(路径)
            print('目录创建成功！')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print('目录已存在！')
            return False

    @staticmethod
    def 主中心登入():
        s= requests.Session()
        UA伪装 = {'Accept': 'application/json, text/plain, */*',
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
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        验证码网址 = 'http://172.18.101.51/api/xt/capture'
        res = s.get(验证码网址)
        路径 = ".\\1.gif"
        with open(路径, 'wb') as t:
            t.write(res.content)
        ocr = ddddocr.DdddOcr()
        with open(路径, 'rb') as f:
            img_bytes = f.read()
        验证码 = ocr.classification(img_bytes)
        网址 = 'http://172.18.101.51/api/xt/login'
        sdata = {'account': '田天文',
                 'pwd_encrypt': 1,
                 'password': 'bFl4eFI5U1poZHl4YyFAMjAyMDlsU0xzVQ==',
                 'code': f'{验证码}'}
        s.post(url=网址, headers=UA伪装, data=sdata)
        return s, UA伪装

    @staticmethod
    def 分中心登入():
        s = requests.Session()
        武汉UA伪装 = {'Accept': 'application/json, text/plain, */*',
                      'Accept-Encoding': 'gzip, deflate, br',
                      'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                      'Cache-Control': 'no-cache',
                      'Connection': 'keep-alive',
                      'Content-Length': '225',
                      'Content-Type': 'application/x-www-form-urlencoded',
                      'Host': '172.18.128.153',
                      'Origin': 'https://172.18.128.153',
                      'Pragma': 'no-cache',
                      'Referer': 'https://172.18.128.153/vadmin/',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        登入参数={'hide_data': '{"update_content":0}',
                  'widget_data': '{"username":"田天文","pwd":"Szhd2020!!!!!!"}',
                  'event_data':'{"name":""}'}
        s.verify = False
        武汉url ='https://172.18.128.153/vadmin/v_login/?s--w=1920&s--h=885'
        s.post(url=武汉url,headers=武汉UA伪装,data=登入参数)
        return s,武汉UA伪装

    @staticmethod
    def 下载(Data, url, 下载内容,s,UA伪装,下载主域):
        路径 = f".\\{下载内容}.xlsx"
        解析 = s.post(url=url, headers=UA伪装, data=Data).json()
        if 'text' in 解析['step']['step_data'].keys():
            time.sleep(100)
            下载url = 下载主域+'/vadmin/v_change_list/xt/xtexport/?s--w=2065&s--h=1145&l-b=导出日志'
            下载Data = {'hide_data': '{"update_content":1}',
                        'widget_data': '{"xt--xtexport--search":null,"table--xt--xtexport":{"value":[],"row":[]},"change_list_select_all":false}'}
            下载解析 = s.post(url=下载url, headers=UA伪装, data=下载Data).json()
            while 下载解析['step'][0]['step_data'][0]['data'][5]['data'][0][5] != '是':
                下载解析 = s.post(url=下载url, headers=UA伪装, data=下载Data).json()
                print('再等一下，莫慌')
                time.sleep(10)
            最后下载地址 = 下载主域 + 下载解析['step'][0]['step_data'][0]['data'][5]['data'][0][6]['event'][0]['step'][0]['step_data']['url']
            文件数据 = s.get(url=最后下载地址)
            with open(路径, 'wb') as t:
                t.write(文件数据.content)
            print('%s下载成功' % 下载内容)

        else:
            findwangzhi = re.compile(r"'url': '(.*)'}}}", re.S)
            下载请求 = s.post(url=url, data=Data)
            返回值 = 下载请求.json()
            下载网址 = re.findall(findwangzhi, str(返回值))[0]
            最后下载地址 = 下载主域 + 下载网址
            print(最后下载地址)
            文件数据 = s.get(url=最后下载地址)
            with open(路径, 'wb') as t:
                t.write(文件数据.content)
            print('%s下载成功' % 下载内容)

    @staticmethod
    def 航标基础数据导出():
        参数='{"scbj":"0","qyjcs":"0","hb_syzt":"1","ssjg__code__startswith":"a0105"}'
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/hb/hbjcxx/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求,verify=False).json()['d']
        武汉分中心航标基础信息列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2,verify=False).json()['d']['results']
                武汉分中心航标基础信息列表.extend(解析2)
        # 创建一个新的列表，用于存储不需要删除的航标基础信息
        # 武汉局_航标基础信息列表 = []
        # for 数据 in 武汉分中心航标基础信息列表:
        #     if not 数据['ssjg_id'].startswith('010502') and \
        #             not 数据['ssjg_id'].startswith('010503') and \
        #             not 数据['ssjg_id'].startswith('010504') and \
        #             not 数据['ssjg_id'].startswith('010505') and \
        #             not 数据['ssjg_id'].startswith('010506') and \
        #             not 数据['ssjg_id'].startswith('010507') and \
        #             not 数据['ssjg_id'].startswith('010508') and \
        #             not 数据['ssjg_id'].startswith('010509') and \
        #             not 数据['ssjg_id'].startswith('010510') and \
        #             not 数据['ssjg_id'].startswith('010523') and \
        #             not 数据['ssjg_id'].startswith('010524') and \
        #             数据['hbmc'] != '':
        #         武汉局_航标基础信息列表.append(数据)
        return  武汉分中心航标基础信息列表

    @staticmethod
    def 航标动态数据导出():
        参数='{"scbj":"0","qyjcs":"0","hb__ssjg__code__startswith":"a0105"}'
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/hb/hbdt/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求,verify=False).json()['d']
        航标动态数据列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                          'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2,verify=False).json()['d']['results']
                航标动态数据列表.extend(解析2)
        # 创建一个新的列表，用于存储不需要删除的航标基础信息
        武汉局_航标动态数据列表 = []
        for 数据 in 航标动态数据列表:
            if 数据['hb_id'] != '':
                武汉局_航标动态数据列表.append(数据)
        return  武汉局_航标动态数据列表

    @staticmethod
    def 终端数据导出():
        参数='{"scbj":"0","ssjg__code__startswith":"a0105"}'
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }

        网址 = 'https://172.18.128.153/api/fw/hb/hbzdxx/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']
        终端数据列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                终端数据列表.extend(解析2)
        # 创建一个新的列表，用于存储不需要删除的航标基础信息
        武汉局_终端数据列表 = []
        for 数据 in 终端数据列表:
            if 数据['hb_id'] != '':
                武汉局_终端数据列表.append(数据)
        return 武汉局_终端数据列表

    @staticmethod
    def 航标器材配置导出():
        参数='{"scbj":"0"}'
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/hb/hbqcpz/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']

        航标器材配置列表 = 解析['results']
        总数 = 解析['paging']['count']

        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                航标器材配置列表.extend(解析2)
        # 创建一个新的列表，用于存储不需要删除的航标基础信息
        武汉局_航标器材配置列表 = []
        unique_ids = set()
        for 数据 in 航标器材配置列表:
            if 数据['hb_id'] != '' and int(数据['sl']) > 0 and ('0107' in 数据['qclx_id'] or '0109' in 数据['qclx_id']):
                if 数据['id'] not in unique_ids:
                    unique_ids.add(数据['id'])
                    武汉局_航标器材配置列表.append(数据)
        return 武汉局_航标器材配置列表

    @staticmethod
    def 航标调度任务导出(查询开始时间,查询结束时间):
        查询开始时间 =查询开始时间-timedelta(days=2)
        查询结束时间 = 查询结束时间 + timedelta(days=1)
        参数 = '{{"scbj":"0","rwsj__gte":"{}","rwsj__lte":"{}","ssjg__code__startswith":"a0105"}}'.format(查询开始时间, 查询结束时间)
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/hb/hbbjrw/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']
        武汉分中心调度任务列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                武汉分中心调度任务列表.extend(解析2)

        定级查找 =  re.compile(r"定级.*?(.)级", re.S)
        分类查找 = re.compile(r"分类.*?(.)类", re.S)

        for 数据 in 武汉分中心调度任务列表:
            if 定级查找.search(数据['rwnr']):
                if re.findall(定级查找, 数据['rwnr'])[0] =='一':
                    数据['定级']=1
                elif re.findall(定级查找, 数据['rwnr'])[0] =='二':
                    数据['定级']=2
                elif re.findall(定级查找, 数据['rwnr'])[0] =='三':
                    数据['定级']=3

            else:
                数据['定级']=None
            if 分类查找.search(数据['rwnr']):
                if re.findall(分类查找, 数据['rwnr'])[0] =='一':
                    数据['分类']=1
                elif re.findall(分类查找, 数据['rwnr'])[0] =='二':
                    数据['分类'] = 2
                elif re.findall(分类查找, 数据['rwnr'])[0] =='三':
                    数据['分类'] = 3
                elif re.findall(分类查找, 数据['rwnr'])[0] =='四':
                    数据['分类'] = 4
            else:
                数据['分类']=None
        return 武汉分中心调度任务列表

    @staticmethod
    def 航标报警历史导出(查询开始时间,查询结束时间):
        参数 = '{{"scbj":"0","qyjcs":"0","czsj__gte":"{}","scbjsj__lte":"{}","hb__ssjg__code__startswith":"a0105"}}'.format(查询开始时间, 查询结束时间)
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/hb/hbbjxxls/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']
        武汉分中心报警历史列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                武汉分中心报警历史列表.extend(解析2)
        return 武汉分中心报警历史列表

    @staticmethod
    def 航标失常数据导出(查询开始时间,查询结束时间):
        参数 = '{{"scbj":"0","wcsj__gte":"{}","wcsj__lte":"{}","hb__ssjg__code__startswith":"a0105"}}'.format(查询开始时间, 查询结束时间)
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/hb/hbscrw/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']
        武汉分中心航标失常列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                武汉分中心航标失常列表.extend(解析2)
        return 武汉分中心航标失常列表

    @staticmethod
    def 失常通告导出(查询开始时间,查询结束时间):
        查询开始时间 =查询开始时间-timedelta(days=7)
        查询结束时间 = 查询结束时间 + timedelta(days=1)
        参数 = '{{"scbj":"0","xf_tglb":"10","ssjg_id":"0105","fbsj__gte":"{}","fbsj__lte":"{}"}}'.format(查询开始时间, 查询结束时间)
        请求 = {'plat_key': '15dda6a7159bf14c8444c994447d2d3eb99f0c7c0f715956992c1d9d99b67892',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'http://172.18.101.51/api/fw/xf/xfhdtg/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求).json()['d']
        武汉局失常恢复通告 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': '15dda6a7159bf14c8444c994447d2d3eb99f0c7c0f715956992c1d9d99b67892',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                武汉局失常恢复通告.extend(解析2)
        for 通告 in 武汉局失常恢复通告:
            # 使用Beautiful Soup去除HTML格式
            soup = BeautifulSoup(通告['tgnr'], 'html.parser')
            通告['tgnr'] = soup.get_text()
        return 武汉局失常恢复通告

    @staticmethod
    def 船舶基础数据导出():
        参数='{"scbj":"0","ssjg__code__startswith":"a0105"}'
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/cb/cbjcsj/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求,verify=False).json()['d']
        武汉分中心船舶基础信息列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2,verify=False).json()['d']['results']
                武汉分中心船舶基础信息列表.extend(解析2)

        return  武汉分中心船舶基础信息列表

    @staticmethod
    def 水位基础信息导出():
        参数 = '{"scbj":"0","sz_swzjb":"1","qyzt":"1","ty_sjsbfs":"2","ssjg__code__startswith":"a0105"}'
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/sz/szswz/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']
        水位站基础信息列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                水位站基础信息列表.extend(解析2)
        return 水位站基础信息列表

    @staticmethod
    def 水位历史导出(水位站ID,查询开始时间,查询结束时间):
        查询开始时间 =查询开始时间-timedelta(minutes=30)
        查询结束时间 = 查询结束时间 - timedelta(minutes=30)
        参数 = '{{"scbj":"0","swz_id":"{}","clsj__gte":"{}","clsj__lte":"{}"}}'.format(水位站ID,查询开始时间, 查询结束时间)
        请求 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
              'page_num': '1',
              'page_size': '1000',
              'params': f'{参数}'
              }
        网址 = 'https://172.18.128.153/api/fw/sz/szswdtls/'
        requests.packages.urllib3.disable_warnings()
        解析 = requests.post(url=网址, data=请求, verify=False).json()['d']
        水位数据列表 = 解析['results']
        总数 = 解析['paging']['count']
        if int(总数) > 1000:
            for i in range(2, int(总数 / 1000) + 2):
                请求2 = {'plat_key': 'c6d060bed6428580667ee4a14482b00c8b73485fd2d8b2b221733fc1b6f1c23b',
                       'page_num': f'{i}',
                       'page_size': '1000',
                       'params': f'{参数}'
                       }
                requests.packages.urllib3.disable_warnings()
                解析2 = requests.post(url=网址, data=请求2, verify=False).json()['d']['results']
                水位数据列表.extend(解析2)
        return  水位数据列表

if __name__ == "__main__":
    最后一天 = datetime.now().date().replace(day=1) - timedelta(days=1)
    第一天 = (datetime.now().date().replace(day=1) - timedelta(days=2)).replace(day=1)
    查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=00, minute=00, second=00)
    查询结束时间 = datetime.combine(最后一天 + timedelta(days=1), datetime.min.time()).replace(hour=00, minute=00, second=00)
    print(查询开始时间,查询结束时间)
    # 查询开始时间 = '2024-04-01'
    # 查询结束时间 = '2024-04-13'
    # # # 数据导出.航标调度任务导出(查询开始时间,查询结束时间)
    # # Session,UA伪装=数据导出.主中心登入()
    # # # 在用url = 'http://172.18.101.51/vadmin/v_export_excel/hb/hbjcxx/?s--w=2133&s--h=1010&l-b=航标基础信息&v_search_v=1&syzt=1'
    # # # 在用Data = {'hide_data': '{"update_content":1}',
    # # #             'widget_data': '{"hb--hbjcxx--search":null,"hb_hbdl":null,"syzt":"1","hb_sbzt":null,"hb_zdybq":null,"sshd_id":null,"sjly":null,"ssjg__code__startswith":null,"table--hb--hbjcxx":{"value":[],"row":[]},"change_list_select_all":true}',
    # # #             'opera_data': '[{"name":"table--hb--hbjcxx","opera":"table_row_opera","data":[]}]'}
    # # 航标失常恢复Data={'hide_data': '{"update_content":1}',
    # #                   'widget_data': '{"hb--hbscrw--search":null,"hb_sclx":null,"hb_scyylx":null,"hb_scxz":null,"wcsj__gte":"%s 00:00:00","wcsj__lte":"%s 00:00:00","sjly":null,"hb__ssjg__code__startswith":null,"table--hb--hbscrw":{"value":[],"row":[]},"change_list_select_all":true}'%(查询开始时间,查询结束时间),
    # #                   'opera_data': '[{"name":"table--hb--hbscrw","opera":"table_row_opera","data":[]}]'}
    # # 航标失常恢复url=f'http://172.18.101.51/vadmin/v_export_excel/hb/hbscrw/?s--w=1365&s--h=870&l-b=航标失常恢复&v_search_v=1&wcsj__gte={查询开始时间}%2000%3A00%3A00&wcsj__lte={查询结束时间}%2000%3A00%3A00'
    # # 下载主域='http://172.18.101.51'
    # # 数据导出.下载(航标失常恢复Data, 航标失常恢复url, '失常恢复',Session, UA伪装,下载主域)
    #
    #
    # Session,UA伪装=数据导出.分中心登入()
    # 数据导出.船舶基础数据导出(Session,UA伪装)
    print(数据导出.水位历史导出(查询开始时间,查询结束时间))
    # print(len(数据导出.水位基础信息导出()))
