from .数据导出 import 数据导出
import pandas as pd
from .统计时间 import 统计表
import numpy as np
from sqlalchemy import text
from datetime import datetime, timedelta
from math import radians, cos, sin, asin, sqrt, atan2, degrees


class 船舶轨迹查询:
    @staticmethod
    def 匹配(sqlsession,库名):
        sql = text(
            f"""SELECT t1.*,t2.ID as 船舶ID ,t2.船舶名称 FROM  失常综合分析 t1 LEFT JOIN `{库名}`.`船舶基础信息` t2 ON t1.单位=t2.单位;"""
        )

        # 执行更新语句
        result = sqlsession.execute(sql)
        # Fetch the results
        data = result.fetchall()
        # Convert the results into a Pandas DataFrame
        失常航标船舶匹配 = pd.DataFrame(data, columns=result.keys())
        return 失常航标船舶匹配

    @staticmethod
    def 主中心船舶轨迹查询(Session, UA伪装, 查询开始时间, 查询结束时间, 船舶ID):
        if 查询结束时间 - 查询开始时间 < timedelta(days=3):
            查询url = "http://172.18.101.51/api/cb/track"
            查询Data = {
                "id": 船舶ID,
                "page_num": "1",
                "page_size": "1000",
                "start_time": 查询开始时间,
                "end_time": 查询结束时间,
            }
            解析 = Session.post(url=查询url, headers=UA伪装, data=查询Data).json()["d"][
                "results"
            ]
        else:
            查询开始时间 = 查询结束时间 - timedelta(days=1)
            查询url = "http://172.18.101.51/api/cb/track"
            查询Data = {
                "id": 船舶ID,
                "page_num": "1",
                "page_size": "1000",
                "start_time": 查询开始时间,
                "end_time": 查询结束时间,
            }
            解析 = Session.post(url=查询url, headers=UA伪装, data=查询Data).json()["d"][
                "results"
            ]
        return 解析

    @staticmethod
    def 分中心船舶轨迹查询(Session, UA伪装, 查询开始时间, 查询结束时间, 船舶ID):
        if 查询结束时间 - 查询开始时间 < timedelta(days=3):
            查询url = "https://172.18.128.153/api/cb/track"
            查询Data = {
                "id": 船舶ID,
                "page_num": "1",
                "page_size": "1000",
                "start_time": 查询开始时间,
                "end_time": 查询结束时间,
            }
            解析 = Session.post(url=查询url, headers=UA伪装, data=查询Data).json()["d"][
                "results"
            ]
        else:
            查询开始时间 = 查询结束时间 - timedelta(days=1)
            查询url = "https://172.18.128.153/api/cb/track"
            查询Data = {
                "id": 船舶ID,
                "page_num": "1",
                "page_size": "1000",
                "start_time": 查询开始时间,
                "end_time": 查询结束时间,
            }
            解析 = Session.post(url=查询url, headers=UA伪装, data=查询Data).json()["d"][
                "results"
            ]
        return 解析

    @staticmethod
    def 航标轨迹查询(Session, UA伪装, 查询开始时间, 查询结束时间, 航标ID):
        if 查询结束时间 - 查询开始时间 < timedelta(days=3):
            查询url = "https://172.18.128.153/api/hb/map/trajectory"
            查询Data = {
                "hb_id": 航标ID,
                "page_num": "1",
                "page_size": "1000",
                "start_time": 查询开始时间,
                "end_time": 查询结束时间,
            }
            解析 = Session.post(url=查询url, headers=UA伪装, data=查询Data).json()["d"][
                "results"
            ]
        else:
            查询开始时间 = 查询结束时间 - timedelta(days=1)
            查询url = "https://172.18.128.153/api/hb/map/trajectory"
            查询Data = {
                "hb_id": 航标ID,
                "page_num": "1",
                "page_size": "1000",
                "start_time": 查询开始时间,
                "end_time": 查询结束时间,
            }
            解析 = Session.post(url=查询url, headers=UA伪装, data=查询Data).json()["d"][
                "results"
            ]
        return 解析

    @staticmethod
    def 计算两点距离(coord1, coord2):
        lon1, lat1 = coord1
        lon2, lat2 = coord2
        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(
            radians, [float(lon1), float(lat1), float(lon2), float(lat2)]
        )
        # haversine 公式
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371.393  # 地球平均半径，单位为公里
        dist = int(c * r * 1000)
        return dist

    @staticmethod
    def 清洗船舶轨迹数据(船舶轨迹):
        船舶轨迹 = sorted(
            船舶轨迹, key=lambda x: datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S")
        )
        最后正常轨迹 = None
        cleaned_data = []
        for i in range(0,len(船舶轨迹)):
            if 最后正常轨迹 is not None:
                dist = 船舶轨迹查询.计算两点距离(船舶轨迹[i]["coordinate"], 最后正常轨迹)
                if dist < 50 or dist > 5000:
                    continue
            cleaned_data.append(船舶轨迹[i])
            最后正常轨迹 = 船舶轨迹[i]["coordinate"]
        return cleaned_data

    @staticmethod
    def 清洗航标轨迹数据(航标轨迹):
        航标轨迹 = sorted(
            航标轨迹, key=lambda x: datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S")
        )
        最后正常轨迹 = None
        cleaned_data = []
        for i in range(0,len(航标轨迹)):
            if 最后正常轨迹 is not None:
                dist = 船舶轨迹查询.计算两点距离(航标轨迹[i]["coordinate"], 最后正常轨迹)
                if dist < 50 or dist > 5000:
                    continue
            cleaned_data.append(航标轨迹[i])
            最后正常轨迹 = 航标轨迹[i]["coordinate"]

        return cleaned_data

    @staticmethod
    def 计算到达现场时间(航标轨迹, 船舶轨迹, 基点经度, 基点纬度):
        到达现场时间 = None
        到达现场位置=None
        if len(航标轨迹) > 2 and len(船舶轨迹) > 2:
            # 船舶轨迹 = 船舶轨迹查询.清洗船舶轨迹数据(船舶轨迹)
            # 航标轨迹 = 船舶轨迹查询.清洗航标轨迹数据(航标轨迹)
            for 航标 in 航标轨迹:
                航标轨迹时间 = datetime.strptime(航标["time"], "%Y-%m-%d %H:%M:%S")
                for 船舶 in 船舶轨迹:
                    船舶轨迹时间 = datetime.strptime(船舶["time"], "%Y-%m-%d %H:%M:%S")
                    if abs((航标轨迹时间 - 船舶轨迹时间).total_seconds()) <= 300:  # 5分钟的秒数
                        航标轨迹位置 = 航标["coordinate"]
                        船舶轨迹位置 = 船舶["coordinate"]
                        距离 = 船舶轨迹查询.计算两点距离(航标轨迹位置, 船舶轨迹位置)

                        if 距离 < 100:
                            到达现场时间 = 船舶轨迹时间
                            到达现场位置=船舶轨迹位置
                            break
                else:
                    continue
                break
        elif len(航标轨迹) <= 2 and len(船舶轨迹) > 2:
            # 船舶轨迹 = 船舶轨迹查询.清洗船舶轨迹数据(船舶轨迹)
            航标轨迹位置 = [基点经度, 基点纬度]
            for 船舶 in 船舶轨迹:
                船舶轨迹时间 = datetime.strptime(船舶["time"], "%Y-%m-%d %H:%M:%S")
                船舶轨迹位置 = 船舶["coordinate"]
                距离 = 船舶轨迹查询.计算两点距离(航标轨迹位置, 船舶轨迹位置)
                if 距离 < 100:
                    到达现场时间 = 船舶轨迹时间
                    到达现场位置=船舶轨迹位置
                    break
        return 到达现场时间,到达现场位置

    @staticmethod
    def 计算垂足坐标(点, 线1, 线2):
        # 解包坐标
        lon1, lat1 = 点
        lon2, lat2 = 线1
        lon3, lat3 = 线2
        # 将经纬度转换为弧度
        lat1, lon1, lat2, lon2, lat3, lon3 = map(
            radians, [lat1, lon1, lat2, lon2, lat3, lon3]
        )

        # 计算向量
        x1, y1 = cos(lat1) * cos(lon1), cos(lat1) * sin(lon1)
        x2, y2 = cos(lat2) * cos(lon2), cos(lat2) * sin(lon2)
        x3, y3 = cos(lat3) * cos(lon3), cos(lat3) * sin(lon3)

        # 2号点到3号点的向量
        dx, dy = x3 - x2, y3 - y2

        # 1号点到2号点的向量
        dx1, dy1 = x1 - x2, y1 - y2

        # 计算投影长度t，即（1号点到2号点的向量）在（2号点到3号点的向量）上的投影长度
        t = (dx1 * dx + dy1 * dy) / (dx * dx + dy * dy)

        # 计算垂足的坐标
        x4, y4 = x2 + t * dx, y2 + t * dy

        # 将笛卡尔坐标转换回经纬度
        lon4 = atan2(y4, x4)
        lat4 = atan2(sin(lat1), cos(lat1) * cos(lon1 - lon4))

        # 转换为度
        lat4, lon4 = map(degrees, [lat4, lon4])

        return lon4, lat4

    @staticmethod
    def 获取里程信息(engine, 船舶轨迹,到达现场位置):
        船舶轨迹 = 船舶轨迹查询.清洗船舶轨迹数据(船舶轨迹)
        df = pd.read_sql_table("节点信息", con=engine, schema="基础数据")
        起点距离列表 = []
        终点距离列表 = []

        for row in df.itertuples():
            起点距离 = 船舶轨迹查询.计算两点距离([row.经度, row.纬度], 船舶轨迹[0]["coordinate"])
            终点距离 = 船舶轨迹查询.计算两点距离([row.经度, row.纬度], 到达现场位置)
            起点距离列表.append(起点距离)
            终点距离列表.append(终点距离)


        起点排序后的索引 = sorted(range(len(起点距离列表)), key=lambda k: 起点距离列表[k])
        起点最小距离索引 = 起点排序后的索引[:2]  # 取排序后的前两个索引
        起点df_rows = df.iloc[起点最小距离索引]

        终点排序后的索引 = sorted(range(len(终点距离列表)), key=lambda k: 终点距离列表[k])
        终点最小距离索引 = 终点排序后的索引[:2]  # 取排序后的前两个索引
        终点df_rows = df.iloc[终点最小距离索引]

        起点垂足=船舶轨迹查询.计算垂足坐标(船舶轨迹[0]["coordinate"], [起点df_rows.iloc[0]['经度'],起点df_rows.iloc[0]['纬度']], [起点df_rows.iloc[1]['经度'],起点df_rows.iloc[1]['纬度']])
        垂足距离=船舶轨迹查询.计算两点距离([起点df_rows.iloc[0]['经度'],起点df_rows.iloc[0]['纬度']], 起点垂足)
        公里数1=起点df_rows.iloc[0]['公里数']+垂足距离/1000

        终点垂足=船舶轨迹查询.计算垂足坐标(到达现场位置, [终点df_rows.iloc[0]['经度'],终点df_rows.iloc[0]['纬度']], [终点df_rows.iloc[1]['经度'],终点df_rows.iloc[1]['纬度']])
        垂足距离=船舶轨迹查询.计算两点距离([终点df_rows.iloc[0]['经度'],终点df_rows.iloc[0]['纬度']], 终点垂足)
        公里数2=终点df_rows.iloc[0]['公里数']+垂足距离/1000
        行驶距离=abs(公里数2-公里数1)
        return 行驶距离
        #259.85


if __name__ == "__main__":
   #  sqlsession, engine, 第一天, 最后一天 = 统计表.上月报()
   #  分中心Session, 分中心UA伪装 = 数据导出.分中心登入()
   #  主中心Session, 主中心UA伪装 = 数据导出.主中心登入()
   #  失常航标船舶匹配 = 船舶轨迹查询.匹配(sqlsession)
   #  sqltext = text('''
   #              UPDATE 失常综合分析
   #              SET
   #                  维护船舶 = :维护船舶,
   #                  到达现场时间 = :到达现场时间,
   #                  现场距离 = :现场距离
   #              WHERE 失常ID = :失常ID
   #          ''')
   #  for i in range(0, len(失常航标船舶匹配)):
   #      失常ID=失常航标船舶匹配.loc[i, "失常ID"]
   #      if 失常ID =='33215834394e4b34bc2094e7e8a9d6df':
   #          航标轨迹=船舶轨迹查询.航标轨迹查询(分中心Session,分中心UA伪装,失常航标船舶匹配.loc[i, "真失常时间"],失常航标船舶匹配.loc[i, "真恢复时间"],失常航标船舶匹配.loc[i, "hb_id"])
   #          船舶轨迹=船舶轨迹查询.船舶轨迹查询(主中心Session,主中心UA伪装,失常航标船舶匹配.loc[i, '真失常时间'],失常航标船舶匹配.loc[i, '真恢复时间'],失常航标船舶匹配.loc[i, '船舶ID'])
   #          到达现场时间,到达现场位置 = 船舶轨迹查询.计算到达现场时间(
   #              航标轨迹,
   #              船舶轨迹,
   #              失常航标船舶匹配.loc[i, '基点经度'],
   #              失常航标船舶匹配.loc[i, '基点纬度']
   #          )
   #          现场距离=None
   #          维护船舶=失常航标船舶匹配.loc[i, "船舶名称"]
   #
   #          if 到达现场时间 is not  None :
   #              现场距离 = 船舶轨迹查询.获取里程信息(engine, 船舶轨迹,到达现场位置)
   #              # 提供参数字典
   #              sqlsession.execute(sqltext, {
   #                  '维护船舶': 维护船舶,
   #                  '到达现场时间': 到达现场时间,
   #                  '现场距离': 现场距离,
   #                  '失常ID': 失常ID
   #              })
   #  # 提交事务
   #  sqlsession.commit()
   #
   # # 关闭会话
   #  sqlsession.close()
   #  航标轨迹=[{'coordinate': [115.066498, 30.246078], 'time': '2024-03-03 13:40:34'}, {'coordinate': [115.066475, 30.246052], 'time': '2024-03-03 13:42:44'}, {'coordinate': [115.066475, 30.246084], 'time': '2024-03-03 13:45:10'}]
   #  船舶轨迹=[{'time': '2024-03-03 13:39:36', 'coordinate': [115.068603, 30.252441]},{'time': '2024-03-03 13:39:36', 'coordinate': [115.068603, 30.252441]},{'time': '2024-03-03 13:39:36', 'coordinate': [115.068603, 30.252441]}, {'time': '2024-03-03 13:40:41', 'coordinate': [115.068164, 30.248583]}, {'time': '2024-03-03 13:41:46', 'coordinate': [115.067285, 30.246484]}, {'time': '2024-03-03 13:42:56', 'coordinate': [115.066601, 30.245898]}, {'time': '2024-03-03 13:44:01', 'coordinate': [115.066894, 30.245703]}, {'time': '2024-03-03 13:45:21', 'coordinate': [115.067333, 30.245117]}, {'time': '2024-03-03 13:46:26', 'coordinate': [115.067773, 30.246337]}, {'time': '2024-03-03 13:47:31', 'coordinate': [115.068701, 30.248291]}, {'time': '2024-03-03 13:48:36', 'coordinate': [115.069433, 30.250146]}, {'time': '2024-03-03 13:49:41', 'coordinate': [115.06997, 30.25205]}, {'time': '2024-03-03 13:50:46', 'coordinate': [115.0708, 30.253857]}, {'time': '2024-03-03 13:51:51', 'coordinate': [115.070947, 30.255078]}, {'time': '2024-03-03 13:52:56', 'coordinate': [115.07124, 30.255517]}, {'time': '2024-03-03 13:54:01', 'coordinate': [115.070947, 30.254833]}, {'time': '2024-03-03 13:55:06', 'coordinate': [115.070556, 30.255273]}, {'time': '2024-03-03 13:56:11', 'coordinate': [115.068408, 30.257128]}]
   #  # 到达现场时间,到达现场位置 = 船舶轨迹查询.计算到达现场时间(航标轨迹,船舶轨迹,115.072,30.2548 )
   #  print(len(船舶轨迹))
   #  清洗船舶轨迹=船舶轨迹查询.清洗船舶轨迹数据(船舶轨迹)
   #  print(len(清洗船舶轨迹))
   #  # print(到达现场时间,到达现场位置)
   分中心Session,分中心UA伪装=数据导出.分中心登入()
   主中心Session,主中心UA伪装=数据导出.主中心登入()
   航标轨迹=船舶轨迹查询.航标轨迹查询(分中心Session,分中心UA伪装,datetime.strptime('2024-04-28 16:56:00','%Y-%m-%d %H:%M:%S'),datetime.strptime('2024-04-29 10:28:21','%Y-%m-%d %H:%M:%S'),'766f3e97282542638d952b9629491aad')
   船舶轨迹= 船舶轨迹查询.主中心船舶轨迹查询(主中心Session, 主中心UA伪装,
                                             datetime.strptime('2024-04-28 16:56:00', '%Y-%m-%d %H:%M:%S'),
                                             datetime.strptime('2024-04-29 10:28:21', '%Y-%m-%d %H:%M:%S'), '733201')

   到达现场时间,到达现场位置 = 船舶轨迹查询.计算到达现场时间(
       航标轨迹,
       船舶轨迹,
      '115.256',
     '30.1594'
   )
   print(到达现场时间,到达现场位置)