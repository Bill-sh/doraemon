import datetime
from django.core.mail import send_mail
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler


def my_job():
    send_mail(
        f'{datetime.datetime.now()} Subject here',
        'Here is the message.',
        'gg576882002@163.com',
        ['gg576882002@outlook.com'],
        fail_silently=False,
    )


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

scheduler.add_job(
    my_job,  # 作业函数
    'cron',  # 触发器类型
    hour=21,
    minute=5,
    id='my_job',  # 作业 id
    replace_existing=True,
)

scheduler.start()
