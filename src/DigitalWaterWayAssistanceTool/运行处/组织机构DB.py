from sqlalchemy import Column,String,Integer
from sqlalchemy import create_engine,DDL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sql import sqlConfig
import pandas as pd
import numpy as np

Base = declarative_base()
sqlsession, engine = sqlConfig.get_sql_session('基础数据')
# 继承 Base类 创建ORM类。直接对应数据表。可以用对象增删改查
class 组织机构(Base):
    __tablename__ = '组织机构'
    ID = Column(Integer(), primary_key=True,unique=True,index=True)  # id
    单位名称=Column(String(255))
    单位=Column(String(255))
    全路径=Column(String(255))
    parent_id=Column(Integer())
    所属单位=Column(String(255))
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    @staticmethod
    def 建表():
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入():
        data= pd.read_excel('机构字典.xlsx', header=0, engine='openpyxl')
        # 自定义列名字典，将原始列名映射到新的列名
        custom_column_names = {
            '主键': 'ID',
            '单位名称': '单位名称',
            '单位简称': '单位',
            '全路径': '全路径',
            'parent_id': 'parent_id',
            '所属单位': '所属单位'
        }
        # 使用 rename 方法替换列名
        data.rename(columns=custom_column_names, inplace=True)
        # 使用 replace 方法将 NaN 替换为 None
        data.replace(np.NaN, None, inplace=True)
        # 将 DataFrame 转换为 JSON 格式
        json_data = data.to_dict(orient='records')
        # 使用bulk_insert_mappings批量导入数据
        sqlsession.bulk_insert_mappings(组织机构, json_data)
        # 提交事务
        sqlsession.commit()
        # 关闭会话
        sqlsession.close()
if __name__ == "__main__":
    组织机构.建表()
    组织机构.数据导入()