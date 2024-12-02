import pymysql
import GetData as gd
from datetime import datetime

def Sql_Execu(sql):
    conn = pymysql.connect(
        host='localhost',  # 数据库服务器的地址
        port=3306,
        user='root',  # 数据库用户名
        password='123456',  # 数据库密码
        database='数字航道质量评估结果'  # 要操作的数据库名
    )
    # 创建一个cursor对象
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    # 关闭cursor和连接
    cursor.close()
    conn.close()
    return result

def SqlInsert():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cdfree=gd.get_cdfree()
    print(cdfree)
    sql1 = f"INSERT INTO 最新探测尺度 VALUES ('{now}','{cdfree[0]}','{cdfree[1]}','{cdfree[2]}','{cdfree[3]}','{cdfree[4]}','{cdfree[5]}','{cdfree[6]}','{cdfree[7]}');"
    Sql_Execu(sql1)
    print("1/8已更新最新探测尺度数据")
    zybcd=gd.get_zybcd()
    sql2 = f"INSERT INTO 周预报尺度 VALUES ('{now}','{zybcd[0]}','{zybcd[1]}','{zybcd[2]}','{zybcd[3]}','{zybcd[4]}','{zybcd[5]}','{zybcd[6]}','{zybcd[7]}');"
    Sql_Execu(sql2)
    print("2/8已更新周预报尺度数据")
    fbnum=gd.get_fbnum()
    sql3= f"INSERT INTO 浮标基础数量 VALUES ('{now}','{fbnum[0]}','{fbnum[1]}','{fbnum[2]}','{fbnum[3]}','{fbnum[4]}','{fbnum[5]}','{fbnum[6]}','{fbnum[7]}')"
    Sql_Execu(sql3)
    print("3/8已更新浮标基础数量数据")
    hbwash=gd.get_hbwash()
    sql4= f"INSERT INTO 浮标已清洗数量 VALUES ('{now}','{hbwash[0]}','{hbwash[1]}','{hbwash[2]}','{hbwash[3]}','{hbwash[4]}','{hbwash[5]}','{hbwash[6]}','{hbwash[7]}')"
    Sql_Execu(sql4)
    print("4/8已更新浮标已清洗数量数据")
    spl = gd.get_hbspsl()
    sql5 = f"INSERT INTO 航标碰损索赔率 VALUES ('{now}','{spl[0]}','{spl[1]}','{spl[2]}','{spl[3]}','{spl[4]}','{spl[5]}','{spl[6]}','{spl[7]}');"
    Sql_Execu(sql5)
    print("5/8已更新航标碰损索赔率数据")
    spje = gd.get_hbspje()
    sql6 = f"INSERT INTO 航标碰损索赔金额 VALUES ('{now}','{spje[0]}','{spje[1]}','{spje[2]}','{spje[3]}','{spje[4]}','{spje[5]}','{spje[6]}','{spje[7]}')"
    Sql_Execu(sql6)
    print("6/8已更新航标碰损索赔金额数据")
    qcbz,qcsj=gd.get_qcreserve()
    sql7 = f"INSERT INTO 器材备品标准 VALUES ('{now}','{qcbz[0]}','{qcbz[1]}','{qcbz[2]}','{qcbz[3]}','{qcbz[4]}')"
    Sql_Execu(sql7)
    print("7/8已更新器材备品标准数据")
    sql8 = f"INSERT INTO 器材备品实际 VALUES ('{now}','{qcsj[0]}','{qcsj[1]}','{qcsj[2]}','{qcsj[3]}','{qcsj[4]}')"
    Sql_Execu(sql8)
    print("8/8已更新器材备品实际数据")

    # cursor.execute(Sql_Return('最新探测尺度',now,cdfree[0],cdfree[1],cdfree[2],cdfree[3],cdfree[4],cdfree[5],cdfree[6],cdfree[7]))
    # cursor.execute(Sql_Return('周预报尺度',now,zybcd[0],zybcd[1],zybcd[2],zybcd[3],zybcd[4],zybcd[5],zybcd[6],zybcd[7]))
    # cursor.execute(Sql_Return('浮标基础数量',now,fbnum[0],fbnum[1],fbnum[2],fbnum[3],fbnum[4],fbnum[5],fbnum[6],fbnum[7]))
    # cursor.execute(Sql_Return('浮标已清洗数量',now,hbwash[0],hbwash[1],hbwash[2],hbwash[3],hbwash[4],hbwash[5],hbwash[6],hbwash[7]))
    #sql = f"INSERT INTO {table} VALUES ('{time}','{a}','{b}','{c}','{d}','{e}','{f}','{g}','{h}')"

def SqlQuery1():
    result_list=[ [], [], [], [], [], [], [], []]
    table_list=['航标碰损索赔率','航标碰损索赔金额','最新探测尺度','周预报尺度','浮标基础数量','浮标已清洗数量']
    for i in range(0,6,1):
        sql=f"SELECT 大沙处,簰洲处,金口处,武汉处,阳逻处,黄冈处,黄石处,蕲州处 FROM {table_list[i]} ORDER BY 统计时间 DESC LIMIT 1"
        result_list[i]=list(Sql_Execu(sql))
    return result_list

def SqlQuery2():
    result_list=[[], []]
    table_list=['器材备品标准', '器材备品实际']
    for i in range(0,2,1):
        sql=f"SELECT 索具,锚具,灯器,标体,浮具 FROM {table_list[i]} ORDER BY 统计时间 DESC LIMIT 1"
        result_list[i]=list(Sql_Execu(sql))
    return result_list
#print(SqlInsert())
#(SqlQuery2())
#SqlInsert()