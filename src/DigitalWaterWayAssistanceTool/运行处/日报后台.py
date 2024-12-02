from 统计时间 import 统计表
from 航标基础数据DB import 航标基础数据
from 航标动态数据DB import 航标动态数据
from 航标终端数据DB import 终端数据
from 航标器材配置DB import 航标器材配置
from 航标报警历史DB import 航标报警历史
from 航标调度任务DB import 航标调度任务
from 航标失常数据DB import 航标失常恢复
from 失常通告DB import 失常恢复通告
from 调度分析SQL import 报警分析,调度分析,最后调度_temp,调度分析_参照_temp
from 失常分析SQL import 失常分析
from 船舶基础信息DB import 船舶基础信息
from 数据导出 import 数据导出
from 失常综合分析DB import 失常综合分析
from 水位数据分析DB import 水位分析
from sql import sqlConfig
from 航标监测覆盖率DB import 航标监测覆盖率
from 航标监测未覆盖明细DB import 航标监测未覆盖明细
from 航标基础信息准确率DB import 航标基础信息准确率
from 航标基础信息错误明细DB import 航标基础信息错误明细
from 调度合格率DB import 调度合格率
from 调度不合格明细DB import 调度不合格明细
from 水位完整率DB import 水位完整率
from 水位正常率DB import 水位正常率
print("开始了")
sqlsession, engine,第一天,最后一天,查询开始时间,查询结束时间,数据库名称 = 统计表.八时日报()
检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')

# //*****************基础信息检查**********************//
航标基础数据.建表(航标基础数据,sqlsession, engine)
航标基础数据.数据导入(sqlsession)
航标基础数据.匹配单位(sqlsession)
航标基础数据.检查标签(sqlsession)
航标动态数据.建表(航标动态数据,sqlsession, engine)
航标动态数据.数据导入(sqlsession)
航标基础数据.匹配动态(sqlsession)
终端数据.建表(终端数据,sqlsession, engine)
终端数据.数据导入(sqlsession)
航标基础数据.匹配终端(sqlsession)
航标器材配置.建表(航标器材配置,sqlsession, engine)
航标器材配置.数据导入(sqlsession)
航标器材配置.合并航标配置(sqlsession)
航标基础数据.匹配航标灯类型(sqlsession)
航标基础数据.检查阈值(sqlsession)

# //*****************航标监测覆盖率**********************//
航标监测覆盖率_数据=航标监测覆盖率.统计(sqlsession)
航标监测覆盖率.数据导入(航标监测覆盖率_数据,检查结果_sqlsession)

# //*****************航标监测未覆盖明细**********************//
航标监测未覆盖明细_数据=航标监测未覆盖明细.明细(sqlsession)
航标监测未覆盖明细.数据导入(航标监测未覆盖明细_数据,检查结果_sqlsession)

# //*****************航标基础信息准确率**********************//
航标基础信息准确率_数据=航标基础信息准确率.统计(sqlsession)
航标基础信息准确率.数据导入(航标基础信息准确率_数据,检查结果_sqlsession)

# //*****************航标基础信息错误明细**********************//
航标基础信息错误明细_数据=航标基础信息错误明细.明细(sqlsession)
航标基础信息错误明细.数据导入(航标基础信息错误明细_数据,检查结果_sqlsession)




# //*****************调度检查**********************//
航标调度任务.建表(航标调度任务,sqlsession, engine)
航标调度任务.数据导入(sqlsession,查询开始时间,查询结束时间)
航标调度任务.匹配调度类型(sqlsession)  #标记特殊调度任务（一类、基点修正、现场作业、综合手段）
航标报警历史.建表(航标报警历史,sqlsession, engine)
航标报警历史.数据导入(sqlsession,查询开始时间,查询结束时间)
航标报警历史.更新报警时长(sqlsession) #把报警航标和航标基础信息匹配，将（标签、浮岸类型、夜间白天、报警时长、单位、航标名称）匹配

最后调度_temp.建表(最后调度_temp,sqlsession, engine) #将调度任务和报警信息匹配
最后调度_temp.数据导入(sqlsession)
最后调度_temp.创建最后调度视图(sqlsession) #报警信息匹配最后一次调度任务
航标报警历史.更新定级(sqlsession) #将（最后调度时间、最后定级、最后分类）匹配到报警表中

#** ** ** ** ** ** ** 按照报警时长和最后定级情况匹配报警分析的类型 ** ** ** ** ** ** ** ** **
报警分析.建表(报警分析,sqlsession, engine)
报警分析.数据导入(sqlsession)  #将报警表匹配报警分析规则表
报警分析.创建报警分析视图(sqlsession)  #取匹配中参考定级最高的
调度分析.建表(调度分析,sqlsession, engine)
调度分析.数据导入(sqlsession) #将匹配后的报警视图按照异常编号匹配调度分析规则表

#** ** ** ** ** ** ** 把用到参照的调度单独分析 ** ** ** ** ** ** ** ** **
调度分析_参照_temp.建表(调度分析_参照_temp,sqlsession, engine)
调度分析_参照_temp.数据导入(sqlsession)
调度分析_参照_temp.创建参照视图(sqlsession) #找到首次参照时间

# #** ** ** ** ** ** ** 合并参照不不参照的两种 ** ** ** ** ** ** ** ** **
调度分析.创建调度分析合并视图(sqlsession) #按阶段将调度任务和报警信息匹配（匹配首次参照时间之前的调度） 合并 首次参照时间之后的调度
调度分析.创建调度分析视图(sqlsession)

# //*****************调度合格率**********************//
调度合格率_数据=调度合格率.统计(sqlsession)
调度合格率.数据导入(调度合格率_数据,检查结果_sqlsession)

# //*****************调度不合格明细**********************//
调度不合格明细_数据=调度不合格明细.明细(sqlsession)
调度不合格明细.数据导入(调度不合格明细_数据,检查结果_sqlsession)





# //*****************失常检查**********************//
航标失常恢复.建表(航标失常恢复,sqlsession, engine)
航标失常恢复.数据导入(sqlsession,查询开始时间,查询结束时间)
航标失常恢复.匹配单位_航标(sqlsession)
航标失常恢复.匹配失常类型(sqlsession)
失常恢复通告.建表(失常恢复通告,sqlsession, engine)
失常恢复通告.数据导入(sqlsession,查询开始时间,查询结束时间)
失常分析.创建失常合并视图(sqlsession)
失常分析.创建失常分析表(sqlsession)
失常分析.创建失常分析视图(sqlsession)
船舶基础信息.建表(船舶基础信息,sqlsession, engine)
船舶基础信息.数据导入(sqlsession)
船舶基础信息.匹配单位(sqlsession)

# //*****************失常综合分析**********************//
失常综合分析.数据导入(检查结果_sqlsession,数据库名称)
分中心Session,分中心UA伪装=数据导出.分中心登入()
主中心Session,主中心UA伪装=数据导出.主中心登入()
try:
    失常综合分析.更新到达时间_分中心(检查结果_sqlsession, 检查结果_engine, 分中心Session, 分中心UA伪装, 数据库名称)
except Exception as e1:
    print(e1)
    try:
        失常综合分析.更新到达时间_主中心(检查结果_sqlsession, 检查结果_engine, 分中心Session,分中心UA伪装, 主中心Session, 主中心UA伪装, 数据库名称)
    except Exception as e2:
        # 如果方案2也失败了，忽略异常
        print(e2)
        pass




# //*****************水位数据检查**********************//
水位分析.分析水位数据(查询开始时间,查询结束时间,检查结果_sqlsession)
小时数=(查询结束时间-查询开始时间).total_seconds()/ 3600
水位完整率_数据=水位完整率.统计(检查结果_sqlsession,小时数,查询开始时间,查询结束时间)
水位完整率.数据导入(水位完整率_数据,检查结果_sqlsession)
水位正常率_数据=水位正常率.统计(检查结果_sqlsession,小时数,查询开始时间,查询结束时间)
水位正常率.数据导入(水位正常率_数据,检查结果_sqlsession)

sqlsession.close()
检查结果_sqlsession.close()




#TODO:阈值基础表，对接前端，可在前端调整
