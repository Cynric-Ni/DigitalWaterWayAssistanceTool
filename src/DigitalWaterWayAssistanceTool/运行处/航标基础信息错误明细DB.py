from sqlalchemy import Column,String,DateTime,Float,text,Integer,Date,Text
from sqlalchemy.orm import declarative_base
from sql import sqlConfig
Base = declarative_base()

class 航标基础信息错误明细(Base):
    __tablename__ = '航标基础信息错误明细'
    ID = Column(String(50), primary_key=True,unique=True)  # id
    检查日期= Column(Date())
    单位 = Column(String(50))
    航标 = Column(String(50))
    标签 = Column(String(50))
    航标灯类型 = Column(String(50))
    厂家 = Column(String(50))
    位移阈值 = Column(Float())
    漂移阈值 = Column(Float())
    终端高电压阈值 = Column(Float())
    终端低电压阈值 = Column(Float())
    航标灯高电压阈值 = Column(Float())
    航标灯低电压阈值 = Column(Float())
    日光阈值 = Column(Float())
    轮询周期 = Column(Float())
    报警周期 = Column(Float())
    问题 = Column(Text)

    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 明细(sqlsession):
        sql = text('''SELECT t1.* FROM (SELECT
	REPLACE(UUID(), '-', '') as ID,
	CURDATE() as 检查日期,
	航标基础数据.单位,
	hbmc AS 航标,
	CONCAT_WS( ', ', CASE WHEN find_in_set( '10', hb_zdybq ) THEN '重点航标' END, CASE WHEN find_in_set( '9', hb_zdybq ) THEN '一般航标' END ) AS 标签,
	航标灯类型,
	厂家,
	wymx AS 位移阈值,
	pymx AS 漂移阈值,
	终端高电压阈值,
	终端低电压阈值,
	航标灯高电压阈值,
	航标灯低电压阈值,
	日光阈值,
	轮询周期,
	报警周期,
	CONCAT_WS(
		', ',
	CASE
			
			WHEN (应为重点航标 = 1 
			AND NOT find_in_set( '10', hb_zdybq )) 
			OR (应为重点航标 IS NULL 
				AND find_in_set( '10', hb_zdybq )) THEN
				'标签设置错误' 
			END,
		CASE
				
				WHEN round(wymx,0) > 理论位移阈值 THEN
				'位移阈值设置错误' 
			END,
		CASE
				
				WHEN round(pymx,0) > 理论漂移阈值 THEN
				'漂移阈值设置错误' 
			END,
		CASE
				
				WHEN round(终端高电压阈值,1) > 理论终端高电压阈值 THEN
				'终端高电压阈值设置错误' 
			END,
		CASE
				
				WHEN round(终端低电压阈值,1) < 理论终端低电压阈值 THEN
				'终端低电压阈值设置错误' 
			END,
		CASE
				
				WHEN round(航标灯高电压阈值,1) > 理论航标灯高电压阈值 THEN
				'航标灯高电压阈值设置错误' 
			END,
		CASE
				
				WHEN round(航标灯低电压阈值,1) < 理论航标灯低电压阈值 THEN
				'航标灯低电压阈值设置错误' 
			END,
		CASE
				
				WHEN round(日光阈值,0) <> 理论日光阈值 THEN
				'日光阈值设置错误' 
			END,
		CASE
				
				WHEN 轮询周期 <> 理论轮询周期 THEN
				'轮询周期设置错误' 
			END,
		CASE
				
				WHEN 报警周期 <> 理论报警周期 THEN
				'报警周期设置错误' 
			END 
			) AS 问题 
		FROM
			`航标基础数据` 
		WHERE
			find_in_set( '11', 航标基础数据.hb_zdybq ) 
			AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
			AND ((应为重点航标 = 1 
					AND NOT find_in_set( '10', hb_zdybq )) 
				OR (应为重点航标 IS NULL 
				AND find_in_set( '10', hb_zdybq )) 
				OR (
					hb_btlx = 1 
				AND (round(wymx,0) > 理论位移阈值 OR round(pymx,0) > 理论漂移阈值 )) 
				OR round(终端高电压阈值,1) > 理论终端高电压阈值
				OR round(终端低电压阈值,1) < 理论终端低电压阈值
				OR round(航标灯高电压阈值,1) > 理论航标灯高电压阈值
				OR round(航标灯低电压阈值,1) < 理论航标灯低电压阈值
			OR round(日光阈值,0) <> 理论日光阈值 
				OR 轮询周期 <> 理论轮询周期
	OR 报警周期 <> 理论报警周期))t1 LEFT JOIN 基础数据.基层处 on t1.`单位`=基础数据.基层处.单位 
	ORDER BY 基础数据.基层处.`序号`''')

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
                异常 = 航标基础信息错误明细(
                    ID=i[0],
                    检查日期=i[1],
                    单位=i[2],
                    航标=i[3],
                    标签=i[4],
                    航标灯类型=i[5],
                    厂家=i[6],
                    位移阈值=i[7],
                    漂移阈值=i[8],
                    终端高电压阈值=i[9],
                    终端低电压阈值=i[10],
                    航标灯高电压阈值=i[11],
                    航标灯低电压阈值=i[12],
                    日光阈值=i[13],
                    轮询周期=i[14],
                    报警周期=i[15],
                    问题=i[16]
                )
                sqlsession.add(异常)
            sqlsession.commit()
if __name__ == '__main__':
    检查结果_sqlsession, 检查结果_engine = sqlConfig.get_sql_session('检查结果')
    航标基础信息错误明细.建表(航标基础信息错误明细,检查结果_sqlsession, 检查结果_engine)
    检查结果_sqlsession.close()