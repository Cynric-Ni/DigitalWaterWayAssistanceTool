from sqlalchemy import Column,String,Integer,DateTime,text,Text,Float
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 船舶基础信息(Base):
    __tablename__ = '船舶基础信息'
    ID = Column(Integer(), primary_key=True,unique=True)  # id
    船舶名称 = Column(String(255))
    类别 = Column(String(255))
    单位ID = Column(Integer())
    单位 = Column(String(255))
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        data= 数据导出.船舶基础数据导出()
        df = pd.DataFrame(data)[["id","cbmc","cb_cblb","dqsydw_id"]]
        df = df[df['cb_cblb'].isin(['1', '2'])].rename(columns={"id": "ID","cbmc":"船舶名称","cb_cblb":"类别","dqsydw_id":"单位ID"})
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # Convert DataFrame to objects
        objects = [船舶基础信息(**row) for _, row in df.iterrows()]
        # Use bulk_save_objects to save objects in a batch
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 匹配单位(sqlsession):
        # 构建跨数据库的 JOIN 子句
        join_clause = text( '''UPDATE 船舶基础信息 
JOIN 基础数据.组织机构 
ON 船舶基础信息.单位ID = 基础数据.组织机构.ID 
SET 船舶基础信息.单位 = 基础数据.组织机构.单位'''
                            )

        # 执行更新语句
        sqlsession.execute(join_clause)


        join_clause = text( '''DELETE FROM 船舶基础信息
WHERE  单位 !='大沙处' and 单位 !='簰洲处' and 单位 !='金口处'  and 单位 !='武汉处' and 单位 !='阳逻处'  and 单位 !='黄冈处'  and 单位 !='黄石处'  and 单位 !='蕲州处';'''
                            )

        # 执行更新语句
        sqlsession.execute(join_clause)

        # 提交事务
        sqlsession.commit()



if __name__ == "__main__":
    sqlsession, engine,第一天,最后一天 = 统计表.上月报()
    船舶基础信息.建表(船舶基础信息,sqlsession, engine)
    船舶基础信息.数据导入(sqlsession)
    船舶基础信息.匹配单位(sqlsession)
