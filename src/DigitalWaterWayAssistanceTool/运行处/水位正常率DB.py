from SrcCode.运行处.sql import sqlConfig
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,DateTime,Float,text,Integer,Date
Base = declarative_base()
class 水位正常率(Base):
    __tablename__ = '水位正常率'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    水位站 = Column(String(50))
    序号 = Column(Integer())
    总数 = Column(Integer())
    正常数 = Column(Integer())
    正常率 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 统计(sqlsession,小时数,查询开始时间,查询结束时间):
        sql = text(f'''SELECT
    数据.ID,
    数据.检查日期,
    数据.站点名称,
		数据.序号,
    数据.总数,
    数据.正常数,
    数据.正常率
FROM (
    SELECT
        REPLACE(UUID(), '-', '') as ID,
        CURDATE() as 检查日期,
        基础数据.水位站.站点名称,
				基础数据.水位站.序号,
        {小时数} AS 总数,
        {小时数} - COALESCE(t1.异常数, 0) AS 正常数,
        ROUND(({小时数} - COALESCE(t1.异常数, 0)) / {小时数} * 100, 2) AS 正常率
    FROM
        基础数据.水位站
    LEFT JOIN (
        SELECT
            水位数据异常.水位站,
            COUNT(*) AS 异常数
        FROM
            水位数据异常
         WHERE 水位数据异常.测量时间 >= '{查询开始时间}' AND 水位数据异常.测量时间 < '{查询结束时间}' 
        GROUP BY
            水位数据异常.水位站
    ) t1 ON 基础数据.水位站.站点名称 = t1.水位站
) AS 数据
UNION ALL
SELECT
    REPLACE(UUID(), '-', '') as ID,
    CURDATE() as 检查日期,
    '总计' AS 水位站,
		9 AS 序号 ,
    SUM(总数) AS 总数,
    SUM(正常数) AS 正常数,
    ROUND(SUM(正常数) / SUM(总数) * 100, 2) AS 正常率
FROM (
    SELECT
        基础数据.水位站.站点名称,
        {小时数} AS 总数,
        {小时数}- COALESCE(t1.异常数, 0) AS 正常数
    FROM
        基础数据.水位站
    LEFT JOIN (
        SELECT
            水位数据异常.水位站,
            COUNT(*) AS 异常数
        FROM
            水位数据异常
                 WHERE 水位数据异常.测量时间 >= '{查询开始时间}' AND 水位数据异常.测量时间 < '{查询结束时间}' 
        GROUP BY
            水位数据异常.水位站
    ) t1 ON 基础数据.水位站.站点名称 = t1.水位站
) AS 总计数据 
ORDER BY 序号;''')

        # 执行查询语句
        result = sqlsession.execute(sql)

        # 获取查询结果
        query_result = result.fetchall()
        # 关闭会话
        sqlsession.close()
        return query_result

    @staticmethod
    def 数据导入(数据,sqlsession):
        if len(数据)!=0:
            for i in 数据:
                异常 = 水位正常率(
                    ID=i[0],
                    检查日期=i[1],
                    水位站=i[2],
                    序号=i[3],
                    总数=i[4],
                    正常数=i[5],
                    正常率=i[6]
                )
                sqlsession.add(异常)
            sqlsession.commit()

    @staticmethod
    def 输出(sqlsession,check_date):
        结果 = sqlsession.query(水位正常率).filter(水位正常率.检查日期 == check_date).order_by(水位正常率.序号).all()
        return  结果
if __name__ == "__main__":
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    水位正常率.建表(水位正常率,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()
