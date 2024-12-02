import requests
import ddddocr
def get_fzx_Session():
    s = requests.Session()
    headers= {'Accept': 'application/json, text/plain, */*',
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
    log_param={'hide_data': '{"update_content":0}',
              'widget_data': '{"username":"张帆","pwd":"Hbc6867#9admin"}',
              'event_data':'{"name":""}'}
    s.verify = False
    url ='https://172.18.128.153/vadmin/v_login/?s--w=1920&s--h=885'
    request=s.post(url=url,headers=headers,data=log_param)
    return request.cookies.get("chang_session")

def get_zzx_Session():
    s = requests.Session()
    headers= {'Accept': 'application/json, text/plain, */*',
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
    code_url= 'http://172.18.101.51/api/xt/capture'
    res = s.get(code_url)
    route = ".\\1.gif"
    with open(route, 'wb') as t:
        t.write(res.content)
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open(route, 'rb') as f:
        img_bytes = f.read()
    code = ocr.classification(img_bytes)
    #print(code)
    log_url = 'http://172.18.101.51/api/xt/login'
    sdata = {'account': '田天文',
             'pwd_encrypt': 1,
             'password': 'bFl4eFI5U1poZHl4YyFAMjAyMDlsU0xzVQ==',
             'code': f'{code}'}
    request=s.post(url=log_url, headers=headers, data=sdata)
    return request.cookies.get("chang_session")

#get_zzx_Session()
#print(get_fzx_Session())

