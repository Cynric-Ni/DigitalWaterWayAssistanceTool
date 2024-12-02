from SrcCode.运行处.航标基础信息准确率DB import 航标基础信息准确率
from SrcCode.运行处.失常综合分析DB import 失常综合分析
from SrcCode.运行处.sql import sqlConfig
from datetime import datetime, timedelta
from SrcCode.运行处.水位完整率DB import 水位完整率
from SrcCode.运行处.水位正常率DB import 水位正常率
class 接口:
    #每天8点10分更新后台数据，如果当前时间在8点30分之前，输出前一天的数据
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    now = datetime.now()
    cutoff_time = now.replace(hour=8, minute=30, second=0, microsecond=0)
    if now < cutoff_time:
        check_date = (now - timedelta(days=1)).date()
    else:
        check_date = now.date()

    @staticmethod
    def 航标基础信息准确率():
        航标基础信息准确率接口=[]
        结果=航标基础信息准确率.输出(接口.检查结果_sqlsession,接口.check_date)
        for i in 结果:
            if i.单位 != '总计':
                航标基础信息准确率接口.append(i.准确率)
        接口.检查结果_sqlsession.close()
        return 航标基础信息准确率接口

    @staticmethod
    def 失常平均恢复时长():
        失常平均恢复时长接口=[]
        结果=失常综合分析.失常综合分析(接口.检查结果_sqlsession)
        for i in 结果:
            if i.单位 != '总计':
                失常平均恢复时长接口.append(i.失常恢复时长)
        接口.检查结果_sqlsession.close()
        return 失常平均恢复时长接口

    @staticmethod
    def 水位数据情况():
        水位数据情况接口=[]
        完整率=水位完整率.输出(接口.检查结果_sqlsession,接口.check_date)
        正常率=水位正常率.输出(接口.检查结果_sqlsession,接口.check_date)
        for i in range(len(完整率)):
            if 完整率[i].水位站 != '总计':
                水位数据情况接口.append([完整率[i].水位站,完整率[i].完整率,正常率[i].正常率])
        接口.检查结果_sqlsession.close()
        return 水位数据情况接口

if __name__ == "__main__":
    print(接口.航标基础信息准确率())
    print(接口.失常平均恢复时长())
    print(接口.水位数据情况())