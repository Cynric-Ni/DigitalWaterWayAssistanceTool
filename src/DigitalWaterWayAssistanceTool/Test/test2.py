import ddddocr
import requests
from bs4 import BeautifulSoup
import Login
def test2():
    cookies = {
        'chang_session': 'raufuor0ujt88hdr6cewqzs7swg69660',
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
    url = 'http://172.18.101.51/vadmin/#v_change_form/bh/bhgzxx/?s--w=1587&s--h=733&id=61a0de58390848cbbc7eeb1610668593&m=3&l-b=%E8%88%AA%E9%81%93%E6%95%B4%E6%B2%BB%E5%BB%BA%E7%AD%91%E7%89%A9%E3%80%81%E8%88%AA%E6%A0%87%E7%AD%89%E8%88%AA%E9%81%93%E8%AE%BE%E6%96%BD%E6%8D%9F%E5%9D%8F&v_search_v=1&czsj__gte=2024-01-01%2000%3A00%3A00&czsj__lte=2024-05-01%2000%3A00%3A00&spqk=1&ssjg__code__startswith=0105&p--bh--bhgzxx=1'

    response = requests.post(url, headers=headers, cookies=cookies)
    print(response.text)
    # soup=BeautifulSoup(response.text,'html.parser')
    # print(soup)
    # image_url=soup.find_all("div")
    # print(image_url)
    # html = response.text
    # print(response.text)
    # html_lxml = etree.HTML(html)
    # datas=html_lxml.xpath('.//div[@class="form-captcha"]')
    #print(datas)
    #with open('C:\\Users\\Administrator\\Desktop\\57e9d951-eced-4502-b5de-791d59479987.gif','rb') as f:
    # with open('blob:http://172.18.101.51/','rb') as f:
    #      img_bytes=f.read()
    # res=ocr.classification(img_bytes)
    # print(res)
test2()



#	blob:http://172.18.101.51/57e9d951-eced-4502-b5de-791d59479987