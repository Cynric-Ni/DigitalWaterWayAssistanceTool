from sqlalchemy import text
from 统计时间 import 统计表


class 航标标签():
    @staticmethod
    def 统计(sqlsession):
        sql = text('''SELECT
	 基础数据.基层处.单位,
	 IFNULL(t1.标签设置错误, 0) AS 标签设置错误
FROM
	基础数据.基层处
	LEFT JOIN (
	SELECT
		航标基础数据.单位,
		sum(
			(应为重点航标 = 1 
				AND (
					NOT find_in_set( '10', 航标基础数据.hb_zdybq ) 
				OR find_in_set( '9', 航标基础数据.hb_zdybq ))) 
			OR ( 应为重点航标 IS NULL AND ( find_in_set( '10', 航标基础数据.hb_zdybq ) OR NOT find_in_set( '9', 航标基础数据.hb_zdybq ) ) ) 
		) AS 标签设置错误 
	FROM
		`航标基础数据` 
	WHERE
		find_in_set( '11', 航标基础数据.hb_zdybq ) 
		AND find_in_set( '13', 航标基础数据.hb_zdybq ) 
	GROUP BY
		航标基础数据.单位 
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
    def 明细(sqlsession):
        sql = text('''SELECT
	单位,
	hbmc AS 航标,
	CONCAT_WS(', ',
		CASE WHEN  find_in_set( '10', hb_zdybq ) THEN '重点航标' END,
		CASE WHEN find_in_set( '9', hb_zdybq ) THEN '一般航标' END
	) AS 标签,
	'标签设置错误' AS 问题详情,
	CURDATE() AS 查询日期 
FROM
	`航标基础数据` 
WHERE
	( find_in_set( '11', 航标基础数据.hb_zdybq ) AND find_in_set( '13', 航标基础数据.hb_zdybq ) ) 
	AND (应为重点航标 = 1 
	AND ( NOT find_in_set( '10', 航标基础数据.hb_zdybq ) OR find_in_set( '9', 航标基础数据.hb_zdybq ) ) 
	OR (应为重点航标 IS NULL AND ( find_in_set( '10', 航标基础数据.hb_zdybq ) OR NOT find_in_set( '9', 航标基础数据.hb_zdybq ))));''')
        # 执行查询语句
        result = sqlsession.execute(sql)

        # 获取查询结果
        query_result = result.fetchall()
        # 关闭会话
        sqlsession.close()
        return query_result


if __name__ == "__main__":
    sqlsession, engine = 统计表.日报()
    覆盖率 = 航标标签.统计(sqlsession)
    print(覆盖率)