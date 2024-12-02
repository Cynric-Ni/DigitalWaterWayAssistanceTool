from sqlalchemy import Column,String,DateTime,Float,text,Integer,Date
from sqlalchemy.orm import declarative_base
from SrcCode.运行处.sql import sqlConfig
Base = declarative_base()

class 航标基础信息准确率(Base):
    __tablename__ = '航标基础信息准确率'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    单位 = Column(String(50))
    序号 = Column(Integer())
    公用航标数 = Column(Integer())
    航标基础数据设置错误数 = Column(Integer())
    准确率 = Column(Float())
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
	t1.总数 as 公用航标数,
	t1.航标基础数据设置错误数,
	ROUND((t1.总数-t1.航标基础数据设置错误数)/t1.总数 * 100, 2)AS 准确率
FROM
	基础数据.基层处
	LEFT JOIN (
	SELECT
		航标基础数据.单位,
		COUNT(*) as 总数,
		SUM(
		CASE
				WHEN ((应为重点航标 = 1 
				AND NOT FIND_IN_SET( '10', hb_zdybq )) 
				OR (应为重点航标 IS NULL 
					AND FIND_IN_SET( '10', hb_zdybq ))) or
					(round(wymx,0) > 理论位移阈值) or
					(round(pymx,0) > 理论漂移阈值) or
					(round(终端高电压阈值,1) > 理论终端高电压阈值) or
					(round(终端低电压阈值,1) < 理论终端低电压阈值) or 
					(round(航标灯高电压阈值,1) > 理论航标灯高电压阈值) or
					(round(航标灯低电压阈值,1) < 理论航标灯低电压阈值) or
					(round(日光阈值,0) <> 理论日光阈值) or
					(轮询周期 <> 理论轮询周期) or 
					(报警周期 <> 理论报警周期) 
					THEN
					1 ELSE 0 
				END 
				) AS 航标基础数据设置错误数
			FROM
				航标基础数据
			WHERE
				find_in_set( '11', 航标基础数据.hb_zdybq ) 
				AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
			GROUP BY
				航标基础数据.单位  
		UNION ALL
			SELECT
				'总计' AS 单位,
				COUNT(*) as 总数,
				SUM(
		CASE
				WHEN ((应为重点航标 = 1 
				AND NOT FIND_IN_SET( '10', hb_zdybq )) 
				OR (应为重点航标 IS NULL 
					AND FIND_IN_SET( '10', hb_zdybq ))) or
					(round(wymx,0) > 理论位移阈值) or
					(round(pymx,0) > 理论漂移阈值) or
					(round(终端高电压阈值,1) > 理论终端高电压阈值) or
					(round(终端低电压阈值,1) < 理论终端低电压阈值) or 
					(round(航标灯高电压阈值,1) > 理论航标灯高电压阈值) or
					(round(航标灯低电压阈值,1) < 理论航标灯低电压阈值) or
					(round(日光阈值,0) <> 理论日光阈值) or
					(轮询周期 <> 理论轮询周期) or 
					(报警周期 <> 理论报警周期) 
					THEN
					1 ELSE 0 
				END 
				) AS 航标基础数据设置错误数
			FROM
				航标基础数据
			WHERE
				find_in_set( '11', 航标基础数据.hb_zdybq ) 
				AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
			) t1 ON 基础数据.基层处.单位 = t1.单位 
	ORDER BY
	基础数据.机构排序 (基础数据.基层处.单位 )''')

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
                异常 = 航标基础信息准确率(
                    ID=i[0],
                    检查日期=i[1],
                    单位=i[2],
                    序号=i[3],
                    公用航标数=i[4],
                    航标基础数据设置错误数=i[5],
                    准确率=i[6]
                )
                sqlsession.add(异常)
            sqlsession.commit()

    @staticmethod
    def 输出(sqlsession,check_date):
        结果 = sqlsession.query(航标基础信息准确率).filter(航标基础信息准确率.检查日期 == check_date).order_by(航标基础信息准确率.序号).all()
        return  结果

if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    航标基础信息准确率.建表(航标基础信息准确率,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()