from sqlalchemy import Column,String,Date,Float,text,Integer
from sqlalchemy.orm import declarative_base
from sql import sqlConfig
Base = declarative_base()

class 航标监测未覆盖明细(Base):
    __tablename__ = '航标监测未覆盖明细'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    单位 = Column(String(50))
    航标 = Column(String(50))
    标签 = Column(String(50))
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 明细(sqlsession):
        sql = text('''SELECT
REPLACE(UUID(), '-', '') as ID,
CURDATE() as 检查日期,
单位,
hbmc AS 航标,
CONCAT_WS(', ',
CASE WHEN  find_in_set( '10', hb_zdybq ) THEN '重点航标' END,
CASE WHEN find_in_set( '9', hb_zdybq ) THEN '一般航标' END
) AS 标签 
FROM
`航标基础数据` 
WHERE
find_in_set( '11', 航标基础数据.hb_zdybq ) 
AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
AND 航标基础数据.终端 IS NULL;''')

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
                异常 = 航标监测未覆盖明细(
                    ID=i[0],
                    检查日期=i[1],
                    单位=i[2],
                    航标=i[3],
                    标签=i[4]
                )
                sqlsession.add(异常)
            sqlsession.commit()
if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    航标监测未覆盖明细.建表(航标监测未覆盖明细,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()