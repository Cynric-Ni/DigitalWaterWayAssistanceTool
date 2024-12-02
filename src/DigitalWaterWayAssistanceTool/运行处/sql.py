from sqlalchemy import create_engine,DDL
from sqlalchemy.orm import sessionmaker


class sqlConfig():

    @staticmethod
    def get_sql_session(数据库名称):
        # 创建引擎，不指定数据库名
        # engine = create_engine("mysql+pymysql://ttw:123456@172.18.128.213:3306/?charset=utf8mb4", pool_pre_ping=True)
        # engine = create_engine("mysql+pymysql://ttw:123456@10.10.10.4:3306/?charset=utf8mb4", pool_pre_ping=True)
        engine= create_engine("mysql+pymysql://root:123456@localhost:3306/?charset=utf8mb4", pool_pre_ping=True)
        # 创建DDL对象
        create_database = DDL(f"CREATE DATABASE IF NOT EXISTS `{数据库名称}`")

        # 获取一个数据库连接，并使用DDL对象执行CREATE DATABASE语句
        with engine.connect() as connection:
            connection.execute(create_database)

        # 创建带有连接选项的引擎
        engine = create_engine(
            # f"mysql+pymysql://ttw:123456@172.18.128.213:3306/{数据库名称}?charset=utf8mb4",
            # f"mysql+pymysql://ttw:123456@10.10.10.4:3306/{数据库名称}?charset=utf8mb4",
            f"mysql+pymysql://root:123456@localhost:3306/{数据库名称}?charset=utf8mb4",
            pool_pre_ping=True,
            echo=False  # 设置为 True 可以打印 SQL 语句
        )

        # 创建并返回会话和引擎
        return sessionmaker(bind=engine)(), engine

if __name__ == "__main__":
    sqlConfig.get_sql_session('失常分析')