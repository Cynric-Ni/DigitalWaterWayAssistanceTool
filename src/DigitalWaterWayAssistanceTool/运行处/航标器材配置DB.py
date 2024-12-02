from sqlalchemy import Column,String,Integer,DateTime,Float,text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表
from 数据导出 import 数据导出
import pandas as pd
import numpy as np
Base = declarative_base()

class 航标器材配置(Base):
    __tablename__ = '航标器材配置'
    id = Column(String(255), primary_key=True,unique=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hb_id = Column(String(255),index=True)
    qclx_id = Column(String(255))
    qcgg_id = Column(String(255))
    qcbh_id = Column(String(255))
    sl = Column(Float())
    flag = Column(Integer())
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }


    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        data= 数据导出.航标器材配置导出()
        # 清理空字符串，将其替换为 None
        df = pd.DataFrame(data)
        df.replace('', None, inplace=True)
        df.replace({np.nan: None}, inplace=True)
        # 将 DataFrame 转换为对象列表
        objects = [航标器材配置(**row) for _, row in df.iterrows()]
        # 使用 bulk_save_objects 批量保存对象
        sqlsession.bulk_save_objects(objects)
        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 合并航标配置(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql1 = text('''UPDATE 航标器材配置 AS target
JOIN (
    SELECT 
        hb_id,
        GROUP_CONCAT(DISTINCT qclx_id ORDER BY qclx_id SEPARATOR ',') AS merged_qclx_id,
        GROUP_CONCAT(DISTINCT qcgg_id ORDER BY qcgg_id SEPARATOR ',') AS merged_qcgg_id
    FROM 航标器材配置
    GROUP BY hb_id
) AS temp
ON target.hb_id = temp.hb_id
SET 
    target.qclx_id = temp.merged_qclx_id,
    target.qcgg_id = temp.merged_qcgg_id;'''
                           )

        # 执行更新语句
        sqlsession.execute(sql1)

        # 提交事务
        sqlsession.commit()

        sql2 = text('''DELETE t1 FROM 航标器材配置 t1
        JOIN 航标器材配置 t2 ON t1.hb_id = t2.hb_id AND t1.id > t2.id;'''
                    )
        # 执行更新语句
        sqlsession.execute(sql2)

        # 提交事务
        sqlsession.commit()


if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()
    航标器材配置.建表(engine)
    航标器材配置.数据导入(sqlsession)

