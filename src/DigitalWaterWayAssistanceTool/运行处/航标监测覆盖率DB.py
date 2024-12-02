from sqlalchemy import Column,String,DateTime,Float,text,Integer,Date
from sqlalchemy.orm import declarative_base
from sql import sqlConfig
Base = declarative_base()

class 航标监测覆盖率(Base):
    __tablename__ = '航标监测覆盖率'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    单位 = Column(String(50))
    序号 = Column(Integer())
    应装 = Column(Integer())
    实装 = Column(Integer())
    覆盖率 = Column(Float())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 统计(sqlsession):
        sql = text('''SELECT
REPLACE(UUID(), '-', '') as ID,
CURDATE() as 检查日期,
基础数据.基层处.单位,
基础数据.基层处.序号,
t1.应装,
t1.实装,
ROUND(t1.实装/t1.应装 * 100, 2) AS 覆盖率
FROM
基础数据.基层处
LEFT JOIN (
SELECT
航标基础数据.单位,
count(航标基础数据.id ) AS 应装,
count(航标基础数据.终端 ) AS 实装
FROM
`航标基础数据` 
WHERE
find_in_set( '11', 航标基础数据.hb_zdybq ) 
AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
GROUP BY
航标基础数据.单位 
UNION ALL
SELECT
'总计' AS 单位,
count(航标基础数据.id ) AS 应装,
count(航标基础数据.终端 ) AS 实装
FROM
`航标基础数据` 		
WHERE
find_in_set( '11', 航标基础数据.hb_zdybq ) 
AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
) t1 ON 基础数据.基层处.单位 = t1.单位 
ORDER BY
基础数据.机构排序 (基础数据.基层处.单位 );''')

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
                异常 = 航标监测覆盖率(
                    ID=i[0],
                    检查日期=i[1],
                    单位=i[2],
                    序号=i[3],
                    应装=i[4],
                    实装=i[5],
                    覆盖率=i[6]
                )
                sqlsession.add(异常)
            sqlsession.commit()

if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    航标监测覆盖率.建表(航标监测覆盖率,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()