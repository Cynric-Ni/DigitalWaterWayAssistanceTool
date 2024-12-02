from 数据导出 import 数据导出
from 统计时间 import 统计表
from datetime import datetime,timedelta
from uuid import uuid4
from 水位数据整点缺失DB import 水位数据整点缺失
from 水位站阈值DB import 水位站阈值
from sql import sqlConfig
from 水位数据异常明细DB import 水位数据异常

class 水位分析:
    @staticmethod
    def 分析水位数据(查询开始时间,查询结束时间,sqlsession):
        重点水位站列表=数据导出.水位基础信息导出()
        基础数据sqlsession, 基础数据engine = sqlConfig.get_sql_session('基础数据')
        for instance in 基础数据sqlsession.query(水位站阈值):
            for i in range(len(重点水位站列表)):
                    水位站ID=重点水位站列表[i]['id']
                    if instance.水位站ID==水位站ID:
                        水位数据列表=数据导出.水位历史导出(水位站ID,查询开始时间,查询结束时间)
                        清洗后水位=水位分析.数据清洗(水位数据列表)
                        缺失整点,异常数据点=水位分析.找出异常数据(清洗后水位,查询开始时间,查询结束时间,instance.阈值)
                        if len(缺失整点)!=0:
                            for 整点 in 缺失整点:
                                # 数据=(str(uuid4()).replace("-", ""),重点水位站列表[i]['swzmc'],整点)
                                new_record = 水位数据整点缺失(
                                    ID=str(uuid4()).replace("-", ""),
                                    水位站=重点水位站列表[i]['swzmc'],
                                    缺失时间=整点
                                )
                                sqlsession.add(new_record)
                        if len(异常数据点)!=0:
                            for 数据 in 异常数据点:
                                异常 = 水位数据异常(
                                    ID=str(uuid4()).replace("-", ""),
                                    水位站=重点水位站列表[i]['swzmc'],
                                    测量时间=数据[0],
                                    水位=数据[1],
                                    差值=数据[2]
                                )
                                sqlsession.add(异常)
                        break
        # 提交会话
        sqlsession.commit()

    @staticmethod
    def 数据清洗(水位数据列表):
        清洗后水位 = {}
        for 数据 in 水位数据列表:
            测量时间 = datetime.strptime(数据['clsj'], '%Y-%m-%d %H:%M:%S')
            if 测量时间.minute >= 50:
                测量时间temp = 测量时间 + timedelta(hours=1)  # 如果分钟>=50，小时加1
                整点时间 = 测量时间temp.replace(minute=0, second=0, microsecond=0)
            else:
                整点时间 = 测量时间.replace(minute=0, second=0, microsecond=0)
            if 10 < 测量时间.minute < 50:
                continue  # 在整点前后10分钟之内的数据不保留
            elif 整点时间 not in 清洗后水位:
                清洗后水位[整点时间] = (测量时间, 数据['scswsd'])
        return 清洗后水位

    @staticmethod
    def 找出异常数据(清洗后水位, 查询开始时间, 查询结束时间, 异常阈值):
        # 生成所有可能整点的集合
        总小时数 = int((查询结束时间 - 查询开始时间).total_seconds() // 3600)
        所有整点 = {查询开始时间 + timedelta(hours=i) for i in range(总小时数)}
        # 将清洗后水位按时间排序
        清洗后水位排序 = dict(sorted(清洗后水位.items(), key=lambda item: item[0]))

        异常数据点 = []
        缺失整点 = set(所有整点)
        最后正常水位 = None

        for 整点时间, (时间, 水位) in 清洗后水位排序.items():
            # 更新缺失整点集合
            if 整点时间 in 缺失整点:
                缺失整点.remove(整点时间)

            # 检查并记录异常水位数据点
            if 最后正常水位 is not None:
                水位差值 = abs(水位 - 最后正常水位)
                if 水位差值 > 异常阈值:
                    异常数据点.append((时间, 水位,水位差值))
                    continue

            最后正常水位 = 水位

        缺失整点 = sorted(list(缺失整点))
        return 缺失整点,异常数据点



if __name__ == "__main__":
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    水位分析.建表(水位分析,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()
