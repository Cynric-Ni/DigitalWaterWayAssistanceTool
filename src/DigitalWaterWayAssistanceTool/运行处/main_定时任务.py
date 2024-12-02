import schedule
import time
import subprocess

def job():
    subprocess.run(["D:\\Ni\\Happynoob\\软件终稿\\SZHDYHZL\\venv\\Scripts\\python.exe", "日报后台.py"])
    # 在这里调用你想要运行的程序或者写下你想要执行的代码
def run_scheduler():
# 安排任务每天早上8点10分执行
    schedule.every().day.at("08:10").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    job()
    # run_scheduler()