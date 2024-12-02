from SrcCode.运行处.sql import sqlConfig
from datetime import datetime, timedelta

class 统计表():
    @staticmethod
    def 八时日报():
        最后一天=datetime.now().date()
        第一天=最后一天-timedelta(days=1)
        数据库名称=f'日报({第一天}至{最后一天})'
        sqlsession, engine = sqlConfig.get_sql_session(数据库名称)
        查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=8, minute=00, second=00)
        查询结束时间 = datetime.combine(最后一天, datetime.min.time()).replace(hour=8, minute=00, second=00)
        return  sqlsession, engine,第一天,最后一天,查询开始时间,查询结束时间,数据库名称

    @staticmethod
    def 周报():
        最后一天=datetime.now().date()
        第一天=最后一天-timedelta(days=7)
        数据库名称 = f'周报({第一天}至{最后一天})'
        sqlsession, engine = sqlConfig.get_sql_session(数据库名称)
        查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=00, minute=00, second=00)
        查询结束时间 = datetime.combine(最后一天+timedelta(days=1), datetime.min.time()).replace(hour=00, minute=00, second=00)
        return  sqlsession, engine,第一天,最后一天,最后一天,查询开始时间,查询结束时间,数据库名称

    @staticmethod
    def 上月报():
        最后一天=datetime.now().date().replace(day=1)- timedelta(days=1)
        第一天=(datetime.now().date().replace(day=1) - timedelta(days=2)).replace(day=1)
        数据库名称 = f'月报({第一天}至{最后一天})'
        查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=00, minute=00, second=00)
        查询结束时间 = datetime.combine(最后一天+timedelta(days=1), datetime.min.time()).replace(hour=00, minute=00, second=00)
        sqlsession, engine = sqlConfig.get_sql_session(数据库名称)
        return  sqlsession, engine,第一天,最后一天,查询开始时间,查询结束时间,数据库名称

    @staticmethod
    def 本月报():
        最后一天=(datetime.now().date().replace(day=1) + timedelta(days=32)).replace(day=1)- timedelta(days=1)
        第一天=datetime.now().date().replace(day=1)
        数据库名称 = f'月报({第一天}至{最后一天})'
        sqlsession, engine = sqlConfig.get_sql_session(数据库名称)
        查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=00, minute=00, second=00)
        查询结束时间 = datetime.combine(最后一天+timedelta(days=1), datetime.min.time()).replace(hour=00, minute=00, second=00)
        return  sqlsession, engine,第一天,最后一天,最后一天,查询开始时间,查询结束时间,数据库名称

    @staticmethod
    def 本年报():
        最后一天=datetime.now().date().replace(month=12, day=31)
        第一天=datetime.now().date().replace(month=1, day=1)
        数据库名称 = f'年报({第一天}至{最后一天})'
        sqlsession, engine = sqlConfig.get_sql_session(数据库名称)
        查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=00, minute=00, second=00)
        查询结束时间 = datetime.combine(最后一天+timedelta(days=1), datetime.min.time()).replace(hour=00, minute=00, second=00)
        return  sqlsession, engine,第一天,最后一天,最后一天,查询开始时间,查询结束时间,数据库名称

    @staticmethod
    def 去年报():
        最后一天=datetime.now().date().replace(year=datetime.now().year - 1, month=12, day=31)
        第一天=datetime.now().date().replace(year=datetime.now().year - 1, month=1, day=1)
        数据库名称 = f'年报({第一天}至{最后一天})'
        sqlsession, engine = sqlConfig.get_sql_session(数据库名称)
        查询开始时间 = datetime.combine(第一天, datetime.min.time()).replace(hour=00, minute=00, second=00)
        查询结束时间 = datetime.combine(最后一天+timedelta(days=1), datetime.min.time()).replace(hour=00, minute=00, second=00)
        return  sqlsession, engine,第一天,最后一天,最后一天,查询开始时间,查询结束时间,数据库名称

if __name__ == "__main__":
    sqlsession, engine,第一天,最后一天,s1,s2,s3=统计表.上月报()
    print(第一天,最后一天)