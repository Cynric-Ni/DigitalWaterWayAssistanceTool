from sqlalchemy import Column,String,Integer,DateTime,Float,text,Text
from sqlalchemy.orm import declarative_base
from 统计时间 import 统计表

Base = declarative_base()

class 报警分析(Base):
    __tablename__ = '报警分析'  # 指定表名
    __mapper_args__={'primary_key':['id']}
    # 假ID  = Column(String(255), primary_key=True,unique=True)  # id
    id = Column(String(255),index=True)  # id
    cjsj = Column(DateTime())
    gxsj = Column(DateTime())
    sjly = Column(Integer())
    scbj = Column(Integer())
    hb_id = Column(String(255))
    sim = Column(String(50))
    hb_bjlx = Column(Integer())
    bjsj = Column(DateTime())
    bjyy = Column(String(255))
    hb_bjdj = Column(String(50))
    ty_bjqrzt = Column(Integer())
    hb_bjyqddj = Column(Integer())
    bjyyjson = Column(String(255))
    bjqrsj = Column(DateTime())
    dbcs = Column(Integer())
    hb_bjdbzt = Column(Integer())
    tzsj = Column(DateTime())
    xysj = Column(DateTime())
    wxyyy = Column(String(255))
    czqk = Column(String(50))
    sfjc = Column(Integer())
    czsj = Column(DateTime())
    gzcdtgz = Column(String(255))
    ssjg_id = Column(String(255))
    tbr_id = Column(String(255))
    tbsj = Column(DateTime())
    zhdjsj = Column(DateTime())
    bjjssj = Column(DateTime())
    bjxcjssj = Column(DateTime())
    flag = Column(Integer())
    yjc = Column(String(255))
    scbjsj = Column(DateTime())
    bhs = Column(Integer())
    sftc = Column(Integer())
    qyjcs = Column(Integer())
    sfyx = Column(Integer())
    xxms = Column(String(255))
    浮标 = Column(Integer())
    重点航标 = Column(Integer())
    夜间 = Column(Integer())
    报警时长 = Column(Float())
    单位 = Column(String(50))
    航标 = Column(String(50))
    最后调度时间 = Column(DateTime())
    最后定级 = Column(Integer())
    最后分类 = Column(Integer())
    异常编号= Column(String(50))
    参考定级 = Column(Integer())
    参考分类 = Column(Integer())
    异常时长下限 = Column(Integer())
    异常时长上限 = Column(Integer())
    总时限 = Column(Integer())
    时限修正 = Column(Integer())
    重要程度 = Column(String(50))
    对照编号 = Column(String(50))
    降级处置类别 = Column(Integer())
    匹配 = Column(Integer())

    __table_args__ = (
        {'mysql_charset': 'utf8mb4'}
    )

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''INSERT INTO 报警分析 SELECT     
	t1.*,
	t2.异常编号,
	t2.参考定级,
	t2.参考分类,
	t2.异常时长下限,
	t2.异常时长上限,
	t2.总时限,
	t2.时限修正,
	t2.重要程度,
	t2.对照编号,
	t2.降级处置类别,
IF
	( t1.最后定级 IS NOT NULL AND t1.最后定级 = t2.参考定级 AND t1.最后分类 = t2.参考分类, 1, 0 ) AS 匹配
FROM
	航标报警历史 t1
	LEFT JOIN 基础数据.航标报警分析 t2 ON ( t1.hb_bjlx = t2.异常种类 )
	AND ( find_in_set( t2.异常原因包括, t1.bjyy ) OR t2.异常原因包括 IS NULL )
	AND ( NOT find_in_set( t2.异常原因排除, t1.bjyy ) OR t2.异常原因排除 IS NULL )
	AND ( t1.夜间 = t2.夜间 OR t2.夜间 IS NULL )
	AND ( t1.报警时长 > t2.异常时长下限 OR t2.异常时长下限 IS NULL )
	AND ( t1.报警时长 <= t2.异常时长上限 OR t2.异常时长上限 IS NULL )
	AND ( t1.浮标 = t2.浮标 OR t2.浮标 IS NULL )
	AND ( t1.重点航标 = t2.重点航标 OR t2.重点航标 IS NULL )
ORDER BY
	id,
	匹配 DESC,
	参考定级 ASC''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 创建报警分析视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''CREATE 
	OR REPLACE VIEW 报警分析视图 AS SELECT
	* 
FROM
	报警分析 
GROUP BY
	id''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


class 调度分析(Base):
    __tablename__ = '调度分析'  # 指定表名
    # 假ID  = Column(String(255), primary_key=True,unique=True)  # id
    __mapper_args__={'primary_key':['id']}
    单位 = Column(String(50))
    id = Column(String(255),  index=True)
    hb_id = Column(String(255))
    航标 = Column(String(50))
    sim = Column(String(50))
    hb_bjlx = Column(Integer())
    scbjsj = Column(DateTime())
    bjyy = Column(String(255))
    czsj = Column(DateTime())
    最后定级 = Column(Integer())
    报警时长 = Column(Float())
    重点航标 = Column(Integer())
    序号 = Column(Integer())
    异常编号 = Column(String(50))
    调度阶段 = Column(Integer())
    最早调度时限 = Column(Integer())
    最晚调度时限 = Column(Integer())
    参照编号 = Column(String(50))
    定级建议 = Column(Integer())
    分类建议 = Column(Integer())
    调度要求 = Column(String(50))
    __table_args__ = (
        {'mysql_charset': 'utf8mb4'}
    )

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''INSERT INTO 调度分析 SELECT 
		t1.单位,
	t1.id,
	t1.hb_id,
	t1.航标,
	t1.sim,
	t1.hb_bjlx,
	t1.scbjsj,
	t1.bjyy,
	t1.czsj,
	t1.最后定级,
	t1.报警时长,
	t1.重点航标,
	t2.* 
FROM
	报警分析视图 t1
	LEFT JOIN 基础数据.调度分析 t2 ON t1.异常编号 = t2.异常编号;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()

        # 关闭会话
        sqlsession.close()

    @staticmethod
    def 创建调度分析合并视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''CREATE 
	OR REPLACE VIEW 调度分析合并视图 AS SELECT
	t1.单位,
	t1.id,
	t1.hb_id,
	t1.航标,
	t1.sim,
	t1.hb_bjlx,
	t1.scbjsj,
	t1.bjyy,
	t1.czsj,
	t1.最后定级 as 合并最后定级,
	t1.报警时长,
	t1.序号,
	t1.异常编号,
	t1.调度阶段,
	t1.最早调度时限,
	t1.最晚调度时限,
	t1.定级建议,
	t1.分类建议,
	t1.调度要求,
	t1.重点航标,
	t2.id as 任务ID,
	t2.rwsj,
	t2.定级,
	t2.分类,
	t2.rwnr,
	t3.首次参照时间,
	NULL AS 参照执行 
FROM
	调度分析 t1	LEFT JOIN 航标调度任务 t2 ON t1.id = t2.bjxx_id 
	AND ((
			unix_timestamp( t2.rwsj ) >= unix_timestamp( t1.scbjsj )+ t1.最早调度时限 * 60 
			AND unix_timestamp( t2.rwsj ) < unix_timestamp( t1.scbjsj ) + t1.最晚调度时限 * 60 
			))
	LEFT JOIN 参照视图 t3 ON t1.id = t3.报警id 
WHERE
	t2.rwsj < t3.首次参照时间 
	OR t3.首次参照时间 IS NULL 
	UNION
SELECT
	t1.单位,
	t1.id,
	t1.hb_id,
	t1.航标,
	t1.sim,
	t1.hb_bjlx,
	t1.scbjsj,
	t1.bjyy,
	t1.czsj,
	t1.最后定级 as 合并最后定级,
	t1.报警时长,
	t2.序号,
	t2.异常编号,
	t2.调度阶段,
	t2.最早调度时限,
	t2.最晚调度时限,
	t2.定级建议,
	t2.分类建议,
	t2.调度要求,
    t1.重点航标,
	t3.id AS 任务id,
	t3.rwsj,
	t3.定级,
    t3.分类,
	t3.rwnr,
	t0.首次参照时间,
	1 AS 参照执行 
FROM
	参照视图 t0
	LEFT JOIN 报警分析视图 t1 ON t0.报警id = t1.id
	LEFT JOIN 基础数据.调度分析 t2 ON t2.序号 > 100
	LEFT JOIN 航标调度任务 t3 ON t1.id = t3.bjxx_id 
	AND (	unix_timestamp( t3.rwsj ) >= unix_timestamp( t1.scbjsj )+ t2.最早调度时限 * 60 
			AND unix_timestamp( t3.rwsj ) < unix_timestamp( t1.scbjsj ) + t2.最晚调度时限 * 60 
			)
WHERE
	t0.首次参照时间 <= t3.rwsj 
	OR t3.rwsj IS NULL 
ORDER BY
	id,
	调度阶段;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()

    @staticmethod
    def 创建调度分析视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''CREATE 
	OR REPLACE VIEW 调度分析视图 AS SELECT
	t1.*,
	t2.*,
		(
	CASE
			
			WHEN t1.定级 = 1  AND t1.分类 = 1 THEN	'一级一类' 
			WHEN t1.定级 = 3  AND t1.分类 = 3 AND t1.报警时长 <= 210 AND t1.rwnr like '%现场作业%'  THEN	'现场作业'  
			WHEN t1.定级 = 3 AND t1.分类 = 3
				AND t1.rwnr like '%综合手段%' 
				AND not t1.rwnr like '%无法%'  
				AND unix_timestamp( t1.rwsj ) >= unix_timestamp( t1.scbjsj )+ 30 * 60 
				AND unix_timestamp( t1.rwsj ) < unix_timestamp( t1.scbjsj ) + 150 * 60 
				THEN '综合手段'  
			WHEN t1.定级 = 3 AND t1.分类 = 4 AND t1.rwnr like '%修正基点%' 
				AND ((t1.重点航标=1 AND unix_timestamp( t1.rwsj ) <= unix_timestamp( t1.scbjsj )+ 30 * 60) 
				OR (t1.重点航标=0 
				AND unix_timestamp( t1.rwsj ) >= unix_timestamp( t1.scbjsj )+ 150 * 60 
				AND unix_timestamp( t1.rwsj ) < unix_timestamp( t1.scbjsj ) + 180 * 60 ))
				THEN '修正基点' 
			ELSE NULL 
				END 
				) AS 调度类型 ,
	(
	CASE
			
			WHEN t2.最后定级 = 1  AND t2.最后分类 = 1 THEN	'一级一类'  
			WHEN t2.最后定级 = 3  AND t2.最后分类 = 3 AND t1.报警时长 <= 210 AND t2.最后调度 like '%现场作业%'  THEN	'现场作业'   
			WHEN t2.最后定级 = 3 AND t2.最后分类 = 3
				AND t2.最后调度 like '%综合手段%' 
				AND not t2.最后调度 like '%无法%'  
				AND unix_timestamp( t2.最后调度时间 ) >= unix_timestamp( t1.scbjsj )+ 30 * 60 
				AND unix_timestamp( t2.最后调度时间 ) < unix_timestamp( t1.scbjsj ) + 150 * 60 
				THEN '综合手段' 
				WHEN t2.最后定级 = 3 AND t2.最后分类 = 4 AND t2.最后调度 like '%修正基点%' 
				AND ((t1.重点航标=1 AND unix_timestamp(t2.最后调度时间 ) <= unix_timestamp( t1.scbjsj )+ 30 * 60) 
				OR (t1.重点航标=0 
				AND unix_timestamp( t2.最后调度时间 ) >= unix_timestamp( t1.scbjsj )+ 150 * 60 
				AND unix_timestamp( t2.最后调度时间 ) < unix_timestamp( t1.scbjsj ) + 180 * 60 ))
				THEN '修正基点'  
				ELSE NULL 
				END 
				) AS 最后调度类型 
			FROM
			调度分析合并视图 t1
	LEFT JOIN 最后调度视图 t2 ON t1.id = t2.报警id ;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


class 最后调度_temp(Base):
    __tablename__ = '最后调度_temp'  # 指定表名
    __mapper_args__={'primary_key':['报警id']}
    报警id = Column(String(255),index=True)
    最后定级时间 = Column(DateTime())
    调度时间 = Column(DateTime())
    最后定级 = Column(Integer())
    定级 = Column(Integer())
    分类 = Column(Integer())
    任务详情= Column(Text())
    __table_args__ = (
        {'mysql_charset': 'utf8mb4'}
    )

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''INSERT INTO 最后调度_temp SELECT
	t1.id AS 报警id,
	t1.zhdjsj AS 最后定级时间,
	t2.rwsj AS 调度时间,
	t1.hb_bjyqddj AS 最后定级,
	t2.定级 AS 定级,
	t2.分类 AS 分类,	
	t2.rwnr AS 任务详情 
FROM
	航标报警历史 t1
	INNER JOIN 航标调度任务 t2 ON t1.id = t2.bjxx_id 
ORDER BY
	报警id,
	调度时间 DESC;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 创建最后调度视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''CREATE 
	OR REPLACE VIEW 最后调度视图 AS SELECT
	报警id AS 报警id,
	调度时间 AS 最后调度时间,
	定级 AS 最后定级,
	分类 AS 最后分类,	
	任务详情 AS 最后调度
FROM
	最后调度_temp 
GROUP BY
	报警id;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


class 调度分析_参照_temp(Base):
    __tablename__ = '调度分析_参照_temp'  # 指定表名
    __mapper_args__={'primary_key':['报警id']}
    报警id = Column(String(255),  index=True)
    调度时间 = Column(DateTime())
    任务详情= Column(Text())
    __table_args__ = (
        {'mysql_charset': 'utf8mb4'}
    )

    def 建表(self,sqlsession,engine):
        sqlsession.execute(text(f"DROP TABLE IF EXISTS {self.__tablename__}"))
        Base.metadata.create_all(engine)

    @staticmethod
    def 数据导入(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''	INSERT INTO 调度分析_参照_temp SELECT  
	t1.id AS 报警id,
	t2.rwsj AS 调度时间,
	t2.rwnr AS 任务详情 
FROM
	航标报警历史 t1
	INNER JOIN 航标调度任务 t2 ON t1.id = t2.bjxx_id 
	AND t2.rwnr LIKE '%参照%' 
ORDER BY
	报警id,
	调度时间
	;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


    @staticmethod
    def 创建参照视图(sqlsession):
        # 构建跨数据库的 JOIN 子句
        sql = text('''CREATE 
	OR REPLACE VIEW 参照视图 AS SELECT
	报警id AS 报警id,
	调度时间 AS 首次参照时间 
FROM
	调度分析_参照_temp 
GROUP BY
	报警id;''')

        # 执行更新语句
        sqlsession.execute(sql)

        # 提交事务
        sqlsession.commit()


class 调度合格率():


    @staticmethod
    def 明细(sqlsession):
        sql = text('''select tt.航标 as 航标,tt.单位 as 所属单位,tt.重点航标 as 是否为重点航标,tt.sim as sim卡号,tt.报警类型 as 报警类型,tt.scbjsj as 报警时间,tt.czsj as 报警消除时间,tt.报警时长 as 报警时长（分钟）,tt.调度阶段 as 调度阶段,tt.定级建议 as 定级建议,tt.分类建议 as 分类建议,tt.rwsj as 调度时间,tt.rwnr as 调度详情,tt.定级 as 实际定级, tt.分类 as 实际分类,tt.调度类型 as 调度类型,tt.参照执行 as 是否参照其他报警调度,tt.首次参照时间 as 首次参照时间,tt.最后调度时间 as 最后调度时间,tt.最后调度 as 最后调度详情,tt.最后定级 as 最后定级,tt.最后分类 as 最后分类 ,tt.最后调度类型 as 最后调度类型 ,tt.调度合格 as 调度是否合格,tt.id as 报警ID,tt.任务ID as 任务ID  from(
SELECT
			t1.*,
			(case when t1.hb_bjlx =1 then '终端故障'
			when t1.hb_bjlx =2 then '参数未同步'
			when t1.hb_bjlx =3 then '航标灯报警'
			when t1.hb_bjlx =4 then '灯通讯报警'
			when t1.hb_bjlx =5 then '电压报警'
			when t1.hb_bjlx =6 then '定位无效'
			when t1.hb_bjlx =7 then '位移报警'
			when t1.hb_bjlx =8 then '漂移报警'
			when t1.hb_bjlx =9 then '超时报警' end )as 报警类型
			,
			(
			CASE
					WHEN t1.rwsj IS NULL THEN 
						CASE
								WHEN t1.报警时长 <= t1.最晚调度时限     
								OR ( t1.最后调度类型 IS NOT NULL AND unix_timestamp(t1.最后调度时间) < unix_timestamp( t1.scbjsj )+ t1.最早调度时限 * 60 ) THEN   
									NULL ELSE 0 
								END 
                    WHEN t1.rwsj IS NOT NULL THEN
                        CASE
                                WHEN length( t1.rwnr )< 20 THEN 0 
                                WHEN t1.rwsj < t1.最后调度时间 AND t1.调度类型 is  null  AND t1.最后调度类型 = '现场作业' THEN 0 
                                WHEN t1.rwsj < t1.最后调度时间 AND  t1.调度类型 != t1.最后调度类型 THEN 0 
																WHEN t1.rwsj < t1.最后调度时间 AND  t1.调度类型 = t1.最后调度类型 THEN 1 					
                                WHEN t1.定级 = t1.定级建议  AND t1.分类 = t1.分类建议   AND ( (t1.参照执行 IS NULL AND t1.rwnr NOT LIKE '%参照%') OR ( t1.参照执行 = 1 AND t1.rwnr LIKE '%参照%' )) THEN  1 
																WHEN (t1.hb_bjlx != 4 and t1.hb_bjlx != 9 and t1.hb_bjlx != 6 and t1.hb_bjlx != 3 and t1.hb_bjlx != 8) or 
																(t1.hb_bjlx = 6 and t1.异常编号='C43') or 
																((t1.hb_bjlx = 3 or t1.hb_bjlx = 8) AND t1.参照执行 is null) AND t1.调度类型 = '综合手段' 
																THEN 0 
                                WHEN t1.rwsj = t1.最后调度时间 AND ( t1.最后调度类型 = '现场作业' OR t1.最后调度类型 = '综合手段'   OR t1.最后调度类型 = '一级一类'  OR t1.最后调度类型 = '修正基点' ) THEN 1

                                ELSE 0 
                                END 
                    END 
                                            ) AS 调度合格 
                                        FROM
                                            调度分析视图 t1) tt
																						where tt.调度合格=0
																				''')

        # 执行查询语句
        result = sqlsession.execute(sql)

        # 获取查询结果
        query_result = result.fetchall()
        # 关闭会话
        sqlsession.close()
        return query_result


if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()