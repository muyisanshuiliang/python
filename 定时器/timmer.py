import time

from apscheduler.schedulers.blocking import BlockingScheduler


def job(father):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(id(father))


class Father(object):
    pass


if __name__ == '__main__':
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式
    father = Father()
    # 采用date的方式，在特定时间只执行一次
    scheduler.add_job(job, 'cron', day='*', second='*/5', args=(father,))

    scheduler.start()
