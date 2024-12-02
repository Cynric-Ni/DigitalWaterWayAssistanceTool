import datetime
import time
import Interface
import AssData
import json
import Interface
import Crawl
import pandas as pd
import numpy as np
import re as re1
from bs4 import BeautifulSoup
#返回当天8时水位及差值
#yearStarDate=
#monthStarDate=datetime.date.today().replace(day=1)
#CurrentDate=datetime.date.today()-datetime.timedelta(days=1)
#-------------------------------------------------------------
year = int(time.strftime("%Y"))
yearStar=datetime.datetime(year,1,1)
#获取每年第一天
yearStarDate= datetime.datetime.strftime(yearStar, "%Y-%m-%d")
#获取每月第一天
monthStarDate=datetime.date.today().replace(day=1)
#获取昨天日期
CurrentDate=datetime.date.today()-datetime.timedelta(days=1)
#-------------------------------------------------------------

def get_sw():  # swz_name
    sw= []
    # 前一天水位
    # yes_day=datetime.date.today()-datetime.timedelta(days=1)#获取昨天日期
    tod_day = datetime.date.today()  # 获取今天日期
    #tod_strtime = tod_day.strftime("%Y-%m-%d 07:40:00")  # 07:50
    tod_endtime = tod_day.strftime("%Y-%m-%d 08:20:00")  # 08:20

    yes_day = tod_day-datetime.timedelta(days=1)  # 获取昨天日期
    yes_strtime = yes_day.strftime("%Y-%m-%d 07:40:00")  # 07:50
    #yes_endtime = yes_day.strftime("%Y-%m-%d 08:20:00")  # 08:20
    # 获取八点水位
    params_str = '{"cjsj__gte":"' + yes_strtime + '","cjsj__lte":"' + tod_endtime + '","swz__ssjg__code__startswith":"a0105"}'
    swzdata = Interface.get_data('https://172.18.128.153/api/fw/sz/szdt8ssw/', params_str)
    length = len(swzdata['d']['results'])
    for i in range(0, length, 1):
        if swzdata['d']['results'][i]['swz_id']=='b8a7e37f0781445ab204a47ed8bf1f40':
            cjsj = swzdata['d']['results'][i]['cjsj']
            scsw = swzdata['d']['results'][i]['scswsd']
            sw.append(scsw)
    diff_sw="{:.2f}".format(sw[1]-sw[0])
    return sw[1],diff_sw
#-------------------------------------------
#左边三模块
def get_swdata():
#水位站整点上数模块，返回二维列表
# [['莫家河', 43.3, 85.8],
# ['簰洲', 83.1, 73.4],
# ['军山', 86.4, 65.2],
# ['汉口', 72.4, 53.9],
# ['阳逻', 72.4, 53.9],
# ['鄂州', 72.4, 53.9],
# ['黄石', 72.4, 53.9],
# ['蕲春', 72.4, 53.9]]
   return ''
def get_hbspsl():
#索赔率   data: [10,20,30,40,50,60,70,80]
#索赔金额 data: [10,20,30,40,50,60,70,80]
#返回两个data
    spcs=[]  #索赔次数
    wcgcs=[]  #未成功次数
    spl=[]  #索赔率
    df=pd.DataFrame()
    #010516黄石   010517黄冈
    jg_code = ['010512', '010513', '010514','01051111', '010515',  '010517', '010516','010518']
    total=[]
    str_date=yearStarDate
    end_date=CurrentDate
    ds,pz,jk,wh,yl,hg,hs,qz=0,0,0,0,0,0,0,0
    for j in range(0,8,1):
        url = f'http://172.18.101.51/vadmin/v_change_list/bh/bhgzxx/?s--w=1416&s--h=651&m=3&l-b=%E8%88%AA%E9%81%93%E6%95%B4%E6%B2%BB%E5%BB%BA%E7%AD%91%E7%89%A9%E3%80%81%E8%88%AA%E6%A0%87%E7%AD%89%E8%88%AA%E9%81%93%E8%AE%BE%E6%96%BD%E6%8D%9F%E5%9D%8F&v_search_v=1&ssjg__code__startswith={jg_code[j]}&czsj__gte={str_date}%2000%3A00%3A00&czsj__lte={end_date}%2000%3A00%3A00'
        response = Crawl.visit_zzx_host(url)
        json1 = json.loads(response.content, strict=False)
        length = len(json1["step"][0]["step_data"][0]["data"][5]["data"])
        spcs.append(length)
        for i in range(0,length,1):
            dw=json1["step"][0]["step_data"][0]["data"][5]["data"][i][1]
            bm=json1["step"][0]["step_data"][0]["data"][5]["data"][i][5]
            sj=json1["step"][0]["step_data"][0]["data"][5]["data"][i][9]
            sf=json1["step"][0]["step_data"][0]["data"][5]["data"][i][10]
            columns=[(dw,bm,sj,sf)]
            if sf=='否':
                if dw=='长江大沙航道处' or dw=='大沙班组':
                    ds+=1
                elif dw == '长江簰洲航道处' or dw == '簰洲班组':
                    pz+=1
                elif dw == '长江金口航道处' or dw == '金口班组':
                    jk+=1
                elif dw == '武桥基地':
                    wh+=1
                elif dw == '长江阳逻航道处' or dw == '阳逻班组':
                    yl+=1
                elif dw == '长江黄冈航道处' or dw == '黄冈班组':
                    hg+=1
                elif dw == '长江黄石航道处' or dw == '黄桥基地':
                    hs+=1
                elif dw == '长江蕲州航道处' or dw == '蕲州班组':
                    qz+=1
            total += columns
            df = pd.DataFrame(total)
    #print('{}{}{}{}{}{}{}{}'.format(ds,pz,jk,wh,yl,hg,hs,qz))
    wcgcs=[ds,pz,jk,wh,yl,hg,hs,qz]
    #print(spcs)
    #print(wcgcs)
    cgcs=[a - b for a,b in zip(spcs,wcgcs)]
    #print(cgcs)
    for a in range(0,8,1):
        splsi="{:.2f}".format(((spcs[a]-wcgcs[a])/spcs[a])*100)
        spl.append(splsi)
    #print(spl)
    return spl

def get_hbspje():
    #获取数据条数、页面数
    sta_date,end_date=yearStarDate,CurrentDate
    print(sta_date)
    print(end_date)
    url = f'http://172.18.101.51/vadmin/v_change_list/bh/bhgzxx/?s--w=1587&s--h=733&m=3&l-b=%E8%88%AA%E9%81%93%E6%95%B4%E6%B2%BB%E5%BB%BA%E7%AD%91%E7%89%A9%E3%80%81%E8%88%AA%E6%A0%87%E7%AD%89%E8%88%AA%E9%81%93%E8%AE%BE%E6%96%BD%E6%8D%9F%E5%9D%8F&v_search_v=1&ssjg__code__startswith=0105&czsj__gte={sta_date}%2000:00:00&czsj__lte={end_date}%2000:00:00&spqk=1'
    response = Crawl.visit_zzx_host(url)
    json1 = json.loads(response.content, strict=False)
    count_Page = \
        json1["step"][0]["step_data"][0]["data"][7]["data"][0]["col_data"][2]["data"][1]["text"]
    res = r'总(.*?)条'
    # print('页数')
    # print(count_Page)
    total_Number = re1.findall(res, count_Page)  # 总共数据条数
    print('数据条数')
    print(total_Number)
    total_Page = round(int(total_Number[0]) / 20)  # 总共页数
    print('总页数')
    print(total_Page)
    count = int(total_Number[0]) % 20  # 最后一页数据条数
    #print('最后一页数据条数')
    #print(count)
    #获取所有碰损航标的id
    id_total=[]
    #获取所有索赔记录id
    for p in range(1,total_Page+1,1):
        #print("page="+str(p))
        id_url=f'http://172.18.101.51/vadmin/v_change_list/bh/bhgzxx/?s--w=1578&s--h=733&p--bh--bhgzxx={p}&m=3&l-b=%E8%88%AA%E9%81%93%E6%95%B4%E6%B2%BB%E5%BB%BA%E7%AD%91%E7%89%A9%E3%80%81%E8%88%AA%E6%A0%87%E7%AD%89%E8%88%AA%E9%81%93%E8%AE%BE%E6%96%BD%E6%8D%9F%E5%9D%8F&v_search_v=1&ssjg__code__startswith=0105&czsj__gte={sta_date}%2000%3A00%3A00&czsj__lte={end_date}%2000%3A00%3A00&spqk=1'
        #http://172.18.101.51/vadmin/v_change_list/bh/bhgzxx/?s--w=1578&s--h=733&p--bh--bhgzxx=8&m=3&l-b=%E8%88%AA%E9%81%93%E6%95%B4%E6%B2%BB%E5%BB%BA%E7%AD%91%E7%89%A9%E3%80%81%E8%88%AA%E6%A0%87%E7%AD%89%E8%88%AA%E9%81%93%E8%AE%BE%E6%96%BD%E6%8D%9F%E5%9D%8F&v_search_v=1&ssjg__code__startswith=0105&czsj__gte=2024-01-01%2000%3A00%3A00&czsj__lte=2024-05-16%2000%3A00%3A00&spqk=1
        response1 = Crawl.visit_zzx_host(id_url)
        id_json = json.loads(response1.content, strict=False)
        id_single=id_json['step'][0]['step_data'][0]['data'][5]['row_id']
        id_total+=id_single
    #根据id获取所有索赔信息
    sp_info=[]
    sp_single_info=[]
    for id in range(0,len(id_total),1):
        #print(id)
        dw=''
        url_je=f'http://172.18.101.51/vadmin/v_change_form/bh/bhgzxx/?s--w=1587&s--h=733&id={id_total[id]}&m=3&l-b=%E8%88%AA%E9%81%93%E6%95%B4%E6%B2%BB%E5%BB%BA%E7%AD%91%E7%89%A9%E3%80%81%E8%88%AA%E6%A0%87%E7%AD%89%E8%88%AA%E9%81%93%E8%AE%BE%E6%96%BD%E6%8D%9F%E5%9D%8F&v_search_v=1&czsj__gte={sta_date}%2000%3A00%3A00&czsj__lte={end_date}%2000%3A00%3A00&spqk=1&ssjg__code__startswith=0105&p--bh--bhgzxx=1'
        re = Crawl.visit_zzx_host(url_je)
        json2 = json.loads(re.content, strict=False)
        hb=json2['step'][0]['step_data'][0]['col_data'][0]['data'][1]['col_data'][0]['data'][0]['col_data'][1]['data'][1]['col_data'][3]['data'][0]['value']
        #print(hb)
        #sj:step[0].step_data[0].col_data[0].data[1].col_data[0].data[2].col_data[1].data[1].col_data[3].data[0].value
        je=json2['step'][0]['step_data'][0]['col_data'][0]['data'][1]['col_data'][0]['data'][2]['col_data'][1]['data'][3]['col_data'][3]['data'][0]['value']
        sj=json2['step'][0]['step_data'][0]['col_data'][0]['data'][1]['col_data'][0]['data'][2]['col_data'][1]['data'][1]['col_data'][3]['data'][0]['value']
        #print("索赔金额")
        #print(je)
        #单位step[0].step_data[0].col_data[0].data[1].col_data[0].data[0].col_data[1].data[1].col_data[1].data[0].value
        dw_id=json2['step'][0]['step_data'][0]['col_data'][0]['data'][1]['col_data'][0]['data'][0]['col_data'][1]['data'][1]['col_data'][1]['data'][0]['value']
        if dw_id=='010512':
            dw = '大沙处'
        elif dw_id == '01051205':
            dw='大沙处'
        elif dw_id == '010513':
            dw = '簰洲处'
        elif dw_id == '01051305':
            dw = '簰洲处'
        elif dw_id == '010514':
            dw = '金口处'
        elif dw_id == '01051405':
            dw = '金口处'
        elif dw_id == '010515':
            dw = '阳逻处'
        elif dw_id == '01051505':
            dw = '阳逻处'
        elif dw_id == '010516':
            dw = '黄石处'
        elif dw_id == '01051610':
            dw = '黄石处'
        elif dw_id == '010517':
            dw = '黄冈处'
        elif dw_id == '01051705':
            dw = '黄冈处'
        elif dw_id == '010518':
            dw = '蕲州处'
        elif dw_id == '01051805':
            dw = '蕲州处'
        elif dw_id == '01051111':
            dw = '武汉处'
        sp_single_info=[(dw,hb,je,sj)]
        print(sp_single_info)
        sp_info +=sp_single_info
    print(len(sp_info))
    df = pd.DataFrame(sp_info, columns=['dw', 'hb', 'money','sj'])
    result=pd.DataFrame(df.groupby('dw').agg({'money':sum}))
    dw1 = ['大沙处', '簰洲处', '金口处', '武汉处', '阳逻处', '黄冈处', '黄石处', '蕲州处']
    #将索引重置为普通列名，默认列名
    result = result.reset_index()
    #print(result)
    sp_result = [0,0,0,0,0,0,0,0]
    for a in range(0,8,1):
        for b in range(0, len(result), 1):
            if(dw1[a]==result.dw.get(b)):
                sp_result[a]=round((result.money.get(b))/10000,4)
            # if(dw1[a]==result.at[b,'dw']):
            #     sp_result[a]=result.at[b,'money']
    print('索赔金额')
    print(sum(sp_result))
    return sp_result
#------------------------------------------
#中间三模块
#养护综合排名
#航标失常恢复
def get_hbschf():
# 各单位恢复时间   data: [10,20,30,40,50,60,70,80]
# 返回一个data
    return ''
#测绘效率完成
#-------------------------------------------
#右边三模块
#获取各单位所有浮标数量(完成)
def get_fbnum():
    hbnum_result = []
    jg_code = ['a010506', 'a010507', 'a010508', 'a010504', 'a010509', 'a010510', 'a010505', 'a010511']
    for i in range(0, len(jg_code), 1):
        params_str = '{"hb_sbzt":"2","hb_btlx":"1","scbj":"0","qyjcs":"0","ssjg__code__startswith":"' + jg_code[i] + '"}'
        all_fb = Interface.get_data('https://172.18.128.153/api/fw/hb/hbjcxx/', params_str)
        length=len(all_fb['d']['results'])
        hbnum_result.append(length)
    #print("浮标数量标准：")
    return hbnum_result
#获取各单位已清洗浮标数量(完成)
def get_hbwash():
# 规定数量   data: [10,20,30,40,50,60,70,80]
# 完成数量   data: [10,20,30,40,50,60,70,80]
# 返回两个data
    #total_hbws=[]
    wash_result=[]
    jg_code=['a010506','a010507','a010508','a010504','a010509','a010510','a010505','a010511']
    #注意内容
    first_day=datetime.date.today().replace(day=1)
    yes_day=datetime.date.today()-datetime.timedelta(days=1)
    str_time = datetime.datetime.strftime(first_day, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strftime(yes_day, "%Y-%m-%d %H:%M:%S")
    # 大沙a010506  簰洲a010507  金口a010508  武汉a010504  阳逻a010509  黄冈a010510  黄石a010505  蕲州a010511
    #params_str = '{"cjsj__gte":"' + str_time + '","cjsj__lte":"' + end_time + '"}'
    #params_str = '{"whsj__gte":"' + str_time + '","whsj__lte":"' + end_time + '","ssjg_id":"0105","hb_whlx":"2"}'
    #params_str = '{"cjsj__gte":"' + str_time + '","cjsj__lte":"' + end_time + '","hb__ssjg__code__startswith":"a010509","hb_whlx":"2"}'
    # params_str = '{"cjsj__gte":"2023-08-01 00:00:00","cjsj__lte":"2023-08-14 00:00:00","ssjg__code__startswith":"a0105"}'
    #hbwash= Interface.get_data('https://172.18.128.153/api/fw/hb/hbwh/', params_str)
    #print(hbwash)
    for j in range(0,len(jg_code),1):
        params_str = '{"cjsj__gte":"' + str_time + '","cjsj__lte":"' + end_time + '","hb__ssjg__code__startswith":"' + jg_code[j] + '","hb_whlx":"2"}'
        hbwash = Interface.get_data('https://172.18.128.153/api/fw/hb/hbwh/', params_str)
        length = len(hbwash['d']['results'])
        wash_result.append(length)
        #print("已清洗:"+str(length))
    #print("航标已清洗数量：")
        #过程细节
        # for i in range(0, length, 1):
        #     id=hbwash['d']['results'][i]['id']
        #     hb_id = hbwash['d']['results'][i]['hb_id']
        #     hb_whsj = hbwash['d']['results'][i]['whsj']
        #     hb_whlx = hbwash['d']['results'][i]['hb_whlx']
        #     whr_id=hbwash['d']['results'][i]['whr_id']
        #     single_hbws = [(hb_whsj, hb_whlx,whr_id)]
        #     total_hbws += single_hbws
        #     print(total_hbws)
    return wash_result
#获取最近探测实际尺度(完成)
def get_cdfree():
# 周预报尺度     data: [10,20,30,40,50,60,70,80]
# 最近探测尺度   data: [10,20,30,40,50,60,70,80]
# 返回两个data
    str_time, end_time = get_weekdate()
    tccd_now = []
    dwcd_dict={'大沙处':'','簰洲处':'','金口处':'','武汉处':'','阳逻处':'','黄冈处':'','黄石处':'','蕲州处':''}
    params_str = '{"cjsj__gte":"' + str_time + '","cjsj__lte":"' + end_time + '","ssjg__code__startswith":"a0105"}'
    # params_str = '{"cjsj__gte":"2023-08-01 00:00:00","cjsj__lte":"2023-08-14 00:00:00","ssjg__code__startswith":"a0105"}'
    hbscale = Interface.get_data('https://172.18.128.153/api/fw/hd/hdsccd/', params_str)
    length = len(hbscale['d']['results'])
    # print("hbscale:"+str(length))
    print(hbscale)
    for i in range(0, length, 1):
        sd_name = AssData.get_sdname(hbscale['d']['results'][i]['hd_id'])
        measure_time = hbscale['d']['results'][i]['cssj']
        min_depth = hbscale['d']['results'][i]['zqss']
        max_depth = hbscale['d']['results'][i]['fxss']
        hd_width = hbscale['d']['results'][i]['hdkd']
        measure_sw = hbscale['d']['results'][i]['sw']
        tc_dw=AssData.get_dwname(hbscale['d']['results'][i]['ssjg_id'])
        single_tccd = [(sd_name, measure_time, min_depth, max_depth, hd_width, measure_sw,tc_dw)]
        tccd_now += single_tccd
    #print(tccd_now.info())
        df=pd.DataFrame(tccd_now)
    #print(df.info)
    #按照单位、时间、水道分别排序
    df=df.sort_values([6,0,1],ascending=[True,True,False])
    #然后去重
    df=df.drop_duplicates(subset=0)
    #按照单位算最小值
    df=df.groupby(6).agg({2:'min'})
    fin_cdfree=df.to_dict()[2]
    #print('最新最小探测尺度：')
    #print(fin_cdfree)
    #按单位排序
    for key1,value1 in fin_cdfree.items():
        for key2,value2 in dwcd_dict.items():
            if key1==key2:
                dwcd_dict[key2]=value1
    #print('按单位排序后尺度：')
    #print(dwcd_dict)
    #将字典的值转为列表返回。
    cdfree_list=list(dwcd_dict.values())
    return cdfree_list
def get_weekdate():  # 返回目前前一周时间
    today =  datetime.datetime.now()- datetime.timedelta(days=1)
    format_today = datetime.datetime.strftime(today, "%Y-%m-%d %H:%M:%S")
    one_week_ago = today - datetime.timedelta(days=10)
    format_weekago = datetime.datetime.strftime(one_week_ago, "%Y-%m-%d %H:%M:%S")
    return format_weekago, format_today
# 获取周预报尺度(完成)
def get_zybcd():  # 获取周预报尺度   strtime,endtime为区域局审批时间
    fin_Data = []
    zcdyb = []
    #strtime, endtime = get_weekdate()
    strtime, endtime = '2024-07-01 10:10:22', '2024-07-12 10:10:22'
    # params_str ='{"gxsj__gte":"2023-11-20 00:00:00","ssjg__code":"a0105"}'
    # params_str = '{"gxsj__gte":"'+strtime+'","gxsj__lte":"'+endtime+'","ssjg__id:0105"}
    # ssjg__code__startswith=0105
    #params_str = '{"cjsj__gte":"' + strtime + '","cjsj__lte":"' + endtime + '","tbjl__ssjg__code":"a0105"}'
    params_str = '{"tcsj__gte":"' + strtime + '","tcsj__lte":"' + endtime + '","tbjl__ssjg__code":"a0105"}'
    cdyb_reslut = Interface.get_data('https://172.18.128.153/api/fw/hd/hdzybcd/', params_str)
    length = len(cdyb_reslut['d']['results'])
    #print(length)
    for i in range(0, length, 1):
        sd_id = cdyb_reslut['d']['results'][i]['hd_id']
        sd_name = AssData.get_sdname(sd_id)
        hed_id = cdyb_reslut['d']['results'][i]['hed_id']
        hed_name = AssData.get_hdname(hed_id)
        hdss = cdyb_reslut['d']['results'][i]['hdss']
        hdkd = cdyb_reslut['d']['results'][i]['hdkd']
        whcdyb = cdyb_reslut['d']['results'][i]['whcdyb']
        cjsj = cdyb_reslut['d']['results'][i]['cjsj']
        single_sdyb = [(sd_name, hed_name,whcdyb ,hdss, hdkd, cjsj)]
        zcdyb += single_sdyb
    #print(zcdyb)
    #如果航道局未审批，数据不会交换至武汉局，将无法获取数据，会报错。
    for j in range(0, 8, 1):
        if j < 4:
            print(zcdyb[1][3])
            fin_Data.append(zcdyb[1][3])   # 切记不能使用fin_Data[i]=''赋值
        else:
            fin_Data.append(zcdyb[0][3])
    #print('周预报尺度：')
    return fin_Data
#获取器材数量(完成)
def get_qcreserve():
# 规定备品数量     data: [10,20,30,40,50,60,70,80]
# 实际备品数量   data: [10,20,30,40,50,60,70,80]
    str_date1,end_date1=get_weekdate()
    str_date=str_date1[0:10]
    end_date=end_date1[0:10]
    bzbp=[]
    sjbp=[]
    url=f'https://172.18.128.153/v_jh/report/jh.v_views.hbc_report/?s--w=1652&s--h=916&bblx=4&start_time={str_date}&end_time={end_date}&ssjg_id=0105&bbcs_btn='
    # Data={'hide_data': '{"update_content":1}',
    #       'event_data': '{"name":""}'}
    response = Crawl.visit_host(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到表格
    table = soup.find('table')
    # 解析表格
    # 初始化一个空的DataFrame
    df = pd.DataFrame()
    # 解析表格数据
    data = []
    for i, tr in enumerate(table.find_all('tr')):
        row_data = []
        for j, td in enumerate(tr.find_all(['td', 'th'])):
            #print(j, td )
            # 假设td是一个包含colspan属性的BeautifulSoup Tag对象
            colspan_value = td.get('colspan', '1')  # 获取colspan属性的值，默认为'1'
            # 清理额外的引号
            colspan_value = colspan_value.replace('\\"', '')
            rowspan_value = td.get('rowspan', '1')  # 获取colspan属性的值，默认为'1'
            # 清理额外的引号
            rowspan_value = rowspan_value.replace('\\"', '')
            # 尝试转换为整数
            colspan = int(colspan_value)
            rowspan = int(rowspan_value)
            rowspan = int(rowspan_value)
            cell_text = td.text
            # 如果单元格有rowspan或colspan，需要将数据填充到相应的行或列
            for k in range(rowspan):
                for l in range(colspan):
                    # 计算实际应该填充的位置
                    row_index = i + k
                    col_index = j + l
                    # 填充数据
                    while len(data) <= row_index:
                        data.append([])
                    while len(data[row_index]) <= col_index:
                        data[row_index].append('')
                    data[row_index][col_index] = cell_text
    # 将解析后的数据转换为DataFrame
    df = pd.DataFrame(data)
    # 清理DataFrame中的空字符串
    df.replace('', pd.NA, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    #print("索具、锚具、灯器、标体、浮具在用")
    #print(df.loc[20, 49],int(df.loc[21, 50])+int(df.loc[23, 49]),df.loc[67, 49],int(df.loc[35, 50])+int(df.loc[36, 49]),df.loc[9,49])
    #print(int(int(df.loc[20, 49])*0.34),int(int(int(df.loc[21, 50])+int(df.loc[23, 49]))*0.51), int(int(df.loc[67, 49])*0.1),int(int(int(df.loc[35, 50]) + int(df.loc[36, 49]))*0.09), int(int(df.loc[9, 49])*0.2))
    #print("索具、锚具、灯器、标体、浮具备用")
    #print(df.loc[20, 50],int(df.loc[21, 51])+int(df.loc[23, 50]),df.loc[67, 50],int(df.loc[35, 51])+int(df.loc[36, 50]),df.loc[9,50])
    bzbp=[round(int(df.loc[20, 49])*0.34/100,2),round(int(int(df.loc[21, 50])+int(df.loc[23, 49]))*0.51/10,2), int(int(df.loc[67, 49])*0.1),int(int(int(df.loc[35, 50]) + int(df.loc[36, 49]))*0.09), int(int(df.loc[9, 49])*0.2)]
    sjbp=[round(int(df.loc[20, 50])/100,2),(int(df.loc[21, 51])+int(df.loc[23, 50]))/10,int(df.loc[67, 50]),int(df.loc[35, 51])+int(df.loc[36, 50]),int(df.loc[9,50])]
    #print(bzbp)
    #print(sjbp)
    # print("标志船在用、备用、损耗：")
    # print(df.loc[9,49],df.loc[9,50],df.loc[9,52])
    # print("钢丝绳在用、备用、损耗：")
    # print(df.loc[20, 49],df.loc[20, 50],df.loc[20, 52])
    # print("铁锚在用、备用、损耗：")
    # print(df.loc[21, 50],df.loc[21, 51],df.loc[21, 53])
    # print("水泥锚在用、备用、损耗：")
    # print(df.loc[23, 49],df.loc[23, 50],df.loc[23, 52])
    # print("锥体在用、备用、损耗：")
    # print(df.loc[35, 50],df.loc[35, 51],df.loc[35, 53])
    # print("罐体在用、备用、损耗：")
    # print(df.loc[36, 49],df.loc[36, 50],df.loc[36, 52])
    # print("航标灯在用、备用、损耗：")
    # print(df.loc[67, 49],df.loc[67, 50],df.loc[67, 52])
    #print('标准备品、实际备品数量')
    return bzbp,sjbp

#print(get_hbspsl())
#print(get_cdfree())
#print(get_zybcd())
#print(get_qcreserve())
#print(get_hbspje())
#print(get_hbwash())




