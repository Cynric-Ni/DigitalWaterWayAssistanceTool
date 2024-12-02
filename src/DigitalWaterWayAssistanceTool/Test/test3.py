import pandas as pd
import datetime
import time
#         money
# dw
# 大沙处  31320.00
# 簰洲处   7700.00
# 蕲州处  93020.00
# 金口处   4060.00
# 阳逻处  48577.56
# 黄冈处   9500.00
# 黄石处  82964.50
# 创建一个DataFrame
# df = pd.DataFrame({
#     'dw': ['大沙处', '簰洲处', '蕲州处', '金口处', '阳逻处', '黄冈处', '黄石处'],
#     'money': ['31320.00', '7700.00', '93020.00', '4060.00', '48577.56', '9500.00', '82964.50']
# })
# dw1 = ['大沙处', '簰洲处', '金口处', '武汉处', '阳逻处', '黄冈处', '黄石处', '蕲州处']
# sp_result = [0,0,0,0,0,0,0,0]
# print(len(df))
# print(df)
# print("************************")
# print(df.dw.get(3))
# print(df.dw.get(2))
# print(df.dw.get(0))

# for a in range(0,8,1):
#     for b in range(0, len(df), 1):
#         if(dw1[a]==df.at[b,'dw']):
#             print(df.at[b,'money'])
#             sp_result[a]=df.at[b,'money']

#print(sp_result)


# import requests
# import os
# import time
# from lxml import etree
# def get_Page(url,headers):
# response = requests.get(url,headers=headers)
# if response.status_code == 200:
# print(response.text)
# return response.text
# return None
# def parse_Page(html,headers):
# html_lxml = etree.HTML(html)
# datas = html_lxml.xpath('.//div[@class="captcha_images_left"]|.//div[@class="captcha_images_right"]')
# item= {}
# 创建保存验证码文件夹
# file = 'D:/******'
# if os.path.exists(file):
# os.chdir(file)
# else:
# os.mkdir(file)
# os.chdir(file)
# for data in datas:
# 验证码名称
# name = data.xpath('.//h3')
# print(len(name))
# 验证码链接
# src = data.xpath('.//div/img/@src')
# print(len(src))
# count = 0
# for i in range(len(name)):
# 验证码图片文件名
# filename = name[i].text + '.jpg'
# img_url = 'https://captcha.com/' + src[i]
# response = requests.get(img_url,headers=headers)
# if response.status_code == 200:
# image = response.content
# with open(filename,'wb') as f:
# f.write(image)
# count += 1
# print('保存第{}张验证码成功'.format(count))
# time.sleep(1)def main():
# url = 'https://captcha.com/captcha-examples.html?cst=corg'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
# html = get_Page(url,headers)
# parse_Page(html,headers)
# if __name__ == '__main__':
# main()
year = int(time.strftime("%Y"))
yearStar=datetime.datetime(year,1,1)
#获取每年第一天
yearStarDate= datetime.datetime.strftime(yearStar, "%Y-%m-%d")
#获取每月第一天
monthStarDate=datetime.date.today().replace(day=1)
#获取昨天日期
CurrentDate=datetime.date.today()-datetime.timedelta(days=1)
print(year)
print(yearStar)
print(yearStarDate)
print(monthStarDate)
print(CurrentDate)