import json

from flask import Flask
from flask import render_template,jsonify
from flask import request
import SqlComm as sc
import Crawl
import GetData
from 运行处.接口 import 接口
import threading
from 运行处.main_定时任务 import  run_scheduler
import CHData

# 启动定时任务的线程
scheduler_thread = threading.Thread(target=run_scheduler)

#Flask(__name__, static_folder='custom_static', # 自定义静态文件目录 template_folder='custom_templates') # 自定义模板文件目录
app=Flask(__name__,static_folder='static',template_folder='templates')
#C:/Users/Administrator/PycharmProjects\SZHDYHZL\venv\SrcCode
#\SrcCode\templates
#/js/MYECHARTS/js/  /venv/SrcCode/templates/

@app.route('/get_data')
def get_data():
    #预报尺度
    result=sc.SqlQuery1()
    spl=result[0]
    spje=result[1]
    tccd=result[2]
    zybcd=result[3]
    fbnum=result[4]
    fbwash=result[5]
    result1=sc.SqlQuery2()
    qcbp=result1[0]
    qcsj=result1[1]
    # 航标基础信息准确率 = 接口.航标基础信息准确率()
    # 失常平均恢复时长 = 接口.失常平均恢复时长()
    # 水位数据情况 = 接口.水位数据情况()
    sjzl=[90, 100, 100, 50, 100, 30, 20, 20]
    swzzd=[
        ['水位站数据', '完整率', '准确率'],
        ['莫家河', 90.0, 99.9],
        ['簰洲', 83.1, 73.4],
        ['军山', 86.4, 65.2],
        ['汉口', 72.4, 90.0],
        ['阳逻', 72.4, 90.0],
        ['鄂州', 72.4, 90.0],
        ['黄石', 72.4, 90.0],
        ['蕲春', 72.4, 90.0]
      ]
    hbschf=[90,90,90,90,90,90,90,90]
    # print(航标基础信息准确率)
    # print(失常平均恢复时长)
    # print(水位数据情况)
    # ybcd=GetData.get_cdfree()
    # #探测尺度
    # tccd=GetData.get_zybcd()
    # #已需清洗航标
    # qxhb=GetData.get_fbnum()
    # #已清洗航标
    # yqxhb=GetData.get_hbwash()

    # 测绘数据
    ch_result = CHData.ch_get_data()


    return jsonify(spl,spje,tccd,zybcd,fbnum,fbwash,qcbp,qcsj,sjzl,swzzd,hbschf,ch_result)
    # return render_template('index.html',tod_sw=tod_sw,diff_sw=diff_sw)
    #return render_template('../index.js', ybcd=ybcd, tccd=tccd)
    #return render_template('index.html',tod_sw=tod_sw,diff_sw=diff_sw)
    #return render_template('index.html', tod_sw=tod_sw, diff_sw=diff_sw,ybcd=json.dumps(ybcd))

@app.route('/')
def index():
    tod_sw, diff_sw = GetData.get_sw();
    return render_template('index.html',tod_sw=tod_sw,diff_sw=diff_sw)

if __name__=='__main__':
    scheduler_thread.start()
    app.run()